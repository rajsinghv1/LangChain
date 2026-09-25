import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model=os.getenv("PRIMARY_MODEL"),
    api_key=os.getenv("AWS_BEARER_TOKEN_BEDROCK"),
    base_url=os.getenv("BEDROCK_BASE_URL")
)

result = llm.invoke("What is the capital of India?")

print(result.content)