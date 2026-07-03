from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

response = client.embeddings.create(
    model="text-embedding-bge-m3",
    input="Hello world"
)

print(response)