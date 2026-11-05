import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model='gpt-oss:20b-cloud',
    base_url='https://ollama.com/v1',
    api_key=os.environ['OLLAMA_API_KEY'],
    temperature=0,
    max_tokens=100,
)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)