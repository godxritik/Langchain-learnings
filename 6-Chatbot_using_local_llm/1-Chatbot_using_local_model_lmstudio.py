from langchain_core.messages import *
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",  # can be any value
    model="qwen2.5-coder-3b-instruct"
)

chat_history = [
    SystemMessage(
        content="You are a Lead Software Engineer specialized in Java Programming language."
    )
]

while True:
    user_input = input("You : ")

    if user_input.lower() == "exit":
        break

    chat_history.append(
        HumanMessage(content=user_input)
    )

    response = model.invoke(chat_history)

    print("AI :", response.content)

    chat_history.append(
        AIMessage(content=response.content)
    )

print("Bye Bro")