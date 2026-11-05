import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model='gpt-oss:20b-cloud',
    base_url='https://ollama.com/v1',
    api_key=os.environ['OLLAMA_API_KEY'],
)

result = llm.invoke("What is the capital of Pakistan?")

print(result.content)