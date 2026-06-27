from urllib import response

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",  # can be any value
    model="qwen2.5-coder-3b-instruct",
    temperature=0
)

chat_prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

chat_history = []
#reading the chat history
with open("chat_history.txt", "r") as file:
    chat_history.extend(file.readlines())

query = input("Enter your query : ")

prompt = chat_prompt_template.invoke({
    "chat_history":chat_history,
    "query":query
})

full_response = ""

for chunk in model.stream(prompt):
    print(chunk.content, end=" ")
    full_response += chunk.content

