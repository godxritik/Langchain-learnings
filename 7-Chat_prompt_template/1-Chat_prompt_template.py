from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

print("running")

chat_prompt_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms what is {topic}")
])

domain = input("Enter domain : ")
topic = input("Enter topic : ")

prompt = chat_prompt_template.invoke({
    "domain" : domain,
    "topic" : topic
})

print(prompt)



