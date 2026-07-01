from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-0.5b-instruct",
    temperature=0,
    max_tokens=1000
)

# result = model.invoke("Write a detailed 300 words article on Black Holes.")
# print(result.content)

for chunk in model.stream("Write a detailed 300 words article on Black Holes."):
    print(chunk.content, end="")

