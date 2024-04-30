import os
from pathlib import Path

def get_api_key() -> str:
    with open("./api_key", "r") as f:
        return f.read().strip()

def dump_code(save_path:Path, code:str):
    with open(save_path, "w") as f:
        f.write(code.encode('ascii', 'ignore').decode('ascii'))