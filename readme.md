# PyCoderGPT


## IMPORTANT NOTICE
You are supposed to run the assistant using you own OpenAI API key.

Put your API key in a file named `api_key`:
```shell
vim api_key
```

## Setup env
```shell
pip install -r requirements.txt
```

## Run basic tests

```Shell
# For using Code Interpreter only
python assistant_CI.py

# For using File Search (Knowledge Retrieval) only
python assistant_KB.py

# For using both tools
python assistant_CIKB.py
```

## Run on datasets
```shell
python run_on_dataset.py
```