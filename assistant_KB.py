import os
from openai import OpenAI
import time
from utils import get_api_key


default_question = "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n"

client = OpenAI(
    api_key=get_api_key(),
)

vector_store = client.beta.vector_stores.create(name="knowledge")
file_paths = ["knowledge.txt"]
file_streams = [open(file_path, "rb") for file_path in file_paths]

file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
    files=file_streams
)

assistant = client.beta.assistants.create(
    name="PyCoderGPT",
    instructions="PyCoderGPT can write/create computer software or applications by providing a specific programming language and basic requirements to the computer. \
                  It has extensive computing and coding experience in many varieties of programming languages and platforms, especially in Python. \
                  When user asks PyCoderGPT to write/create a program or a function, PyCoderGPT will generate the code based on the user's request and its own expertise follow the following steps: \
                  As a professional engineer, PyCoderGPT will provide Google-style docstrings and explanation comments in the code it generates. \
                  PyCoderGPT can explore knowledge base and retrieve relevant information to help it generate code. \
                  PyCoderGPT will always provide a runnable code without any placeholders.",
    tools=[{"type": "file_search"}],
    # model="gpt-3.5-turbo-1106"
    model="gpt-4-1106-preview",
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}}
)

def generate_code(question:str=default_question) -> str:
    thread = client.beta.threads.create()

    user_prompt = f"Please check 'knowledge' first to see if there's any similar questions for inspiration, show the analysis result. Then {question}"
    print(user_prompt)

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_prompt
    )

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id)

    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

    while run.status != "completed":
        print(run.status)
        time.sleep(30)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )

    response = messages.data[0].content[0].text.value
    try:
        code = response.split("```python")[1].split("```")[0]
    except Exception as e:
        code = None

    if not code:
        print("No code found in response.")
        res_str = ""
    else:
        res_str = code

    return res_str

if __name__ == "__main__":
    res_str = generate_code()
    print(res_str)
