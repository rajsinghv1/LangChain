import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model=os.getenv("PRIMARY_MODEL"),
    api_key=os.getenv("AWS_BEARER_TOKEN_BEDROCK"),
    base_url=os.getenv("BEDROCK_BASE_URL"),
    temperature=0.7,
    max_completion_tokens=300
)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)