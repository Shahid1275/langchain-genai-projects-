# LangChain GenAI Projects

Practice code and mini-projects built while learning LangChain and GenAI concepts. Each folder is a self-contained topic.

## Contents

- `langchain-models-master` — LLMs, chat models, embedding models
- `langchain-prompts-main` — Prompt templates, chat prompts, chatbot
- `langchain-output-parsers-main` — Output parsers (JSON, Pydantic, structured, string)
- `langchain-structured-output-main` — Structured output with Pydantic/TypedDict/JSON schema
- `langchain-document-loaders-main` — Document loaders (CSV, PDF, text, web, directory)
- `langchain-text-splitters-main` — Text splitting strategies

## Setup

Each folder has its own dependencies. Create a virtual environment inside the folder you want to run, install requirements if present, and add a `.env` file with your API keys (ignored by git).

```bash
cd <folder-name>
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
