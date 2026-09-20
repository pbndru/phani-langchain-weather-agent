# LangChain + LM Studio sample

This project is a beginner-friendly LangChain learning path that connects to LM Studio through its OpenAI-compatible local server.

## Prerequisites

- LM Studio installed
- A model loaded in LM Studio
- The local server started in LM Studio on `http://localhost:1234`
- Python 3.10+

## Setup

```powershell
cd C:\Users\pbndr\projects\phani-langchain-weather-agent
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Optional environment variables

```powershell
$env:LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
$env:LM_STUDIO_API_KEY = "lm-studio"
$env:LM_STUDIO_MODEL = "google/gemma-4-e4b"
```

## Learning order

Start with the smallest example and move forward only when each step makes sense.

1. `01_basic_model.py`
	Plain model call. Learn what `ChatOpenAI` returns.
2. `02_prompt_chain.py`
	Prompt template plus LCEL chain. Learn `prompt | model | parser`.
3. `03_tool_calling.py`
	Direct tool calling without a full agent. Learn how models request tools.
4. `app.py`
	Agent-based version. Useful after the first three examples are clear.

## Run

Run the files in this order:

```powershell
python 01_basic_model.py
python 02_prompt_chain.py
python 03_tool_calling.py
python app.py
```

If your LM Studio model needs a different API model name, change `LM_STUDIO_MODEL` before running.

## What to notice

- In `01_basic_model.py`, focus on the `model.invoke(...)` call and the `response.content` value.
- In `02_prompt_chain.py`, focus on how prompt variables flow into the chain.
- In `03_tool_calling.py`, focus on `response.tool_calls` and how a tool result is sent back.
- In `app.py`, focus on how the agent hides some of the manual tool orchestration.
