import json
import os
import errno
from pathlib import Path
from utils import dump_code
from assistant_CIKB import generate_code
import time

dataset = "MBPP" # "HE" or "MBPP"

# choose dataset, get corresponding dataset config
if dataset == "HE":
    dataset_file = "./dataset/HumanEval.jsonl"
    question_key = "prompt"
    test_key = "test"
    task_id_key = "task_id"
    def get_task_id(question_dict:dict, task_id_key:str) -> str:
        return question_dict[task_id_key].split("/")[-1].zfill(3)
    def gen_question(question:str) -> str:
        return f"Finish the following function for me: \n {question}"
elif dataset == "MBPP":
    dataset_file = "./dataset/MBPP.jsonl"
    question_key = "prompt"
    test_key = "test"
    task_id_key = "task_id"
    def get_task_id(question_dict:dict, task_id_key:str) -> str:
        return question_dict[task_id_key]
    def gen_question(question:str) -> str:
        return f"{question}"
else:
    raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), dataset)

# load all questions
questions = []
with open(dataset_file, "r") as f:
    for line in f:
        data = json.loads(line)
        questions.append(data)

# set save path
save_path = Path(f"./cases")
if not os.path.exists(save_path):
    os.makedirs(save_path)

start_time = time.time()
# idxs = [266, 272, 283, 295, 300, 314, 323, 336, 345, 346, 357, 360, 377, 379, 388, 394, 406]
# running_questions = [questions[i] for i in idxs]
running_questions = questions[:10]
for i in running_questions:
    print(f"Task ID: {i[task_id_key]}")
    question = i[question_key]
    test_cases = i[test_key]

    task_id = f"{dataset}_" + get_task_id(i, task_id_key)
    question  = gen_question(question)

    # ask assistant to generate code
    res_str = generate_code(question)

    # dump code to file
    res_path = os.path.join(save_path, f"case_{task_id}.py")
    dump_code(save_path=res_path, code=res_str)
end_time = time.time()
print(f"Time elapsed: {end_time-start_time}s")
print(f"Average time per case: {(end_time-start_time)/len(running_questions)}s")