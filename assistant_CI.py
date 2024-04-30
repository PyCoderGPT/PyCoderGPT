import os
from openai import OpenAI
import time
from utils import get_api_key


default_question = "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n"

client = OpenAI(
    api_key=get_api_key(),
)

assistant = client.beta.assistants.create(
    name="PyCoderGPT",
    instructions="PyCoderGPT can write/create computer software or applications by providing a specific programming language and basic requirements to the computer. \
                  It has extensive computing and coding experience in many varieties of programming languages and platforms, especially in Python. \
                  When user asks PyCoderGPT to write/create a program or a function, PyCoderGPT will generate the code based on the user's request and its own expertise follow the following steps: \
                  1. In background, analyse the requirements and generate the code along with several test cases (make sure the test cases are correct). \
                  2. Run the generated code and make necessary improvements if there's any problem. \
                  3. Repeat Step 2 until every test case can run correctly \
                  4. Don't forget to print and only print the final code with test cases to run to user. \
                  As a professional engineer, PyCoderGPT will provide Google-style docstrings and explanation comments in the code it generates. \
                  PyCoderGPT will always provide a runnable code without any placeholders.",
    tools=[{"type": "code_interpreter"}],
    # model="gpt-3.5-turbo-1106"
    model="gpt-4-1106-preview"
)

def generate_code(question:str=default_question) -> str:
    thread = client.beta.threads.create()

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=f"{question}"
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