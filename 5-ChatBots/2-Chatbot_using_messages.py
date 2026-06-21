from langchain_core.messages import *
from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1)

chat_history = [
    SystemMessage("You are a Lead Software engineer specialised in Java Programming language:")
]

while True:
    user_input = input("You : ")
    if user_input == "exit":
        break
    chat_history.append(HumanMessage(user_input))
    response = model.invoke(chat_history)
    print("AI :", response.content)
    chat_history.append(AIMessage(response.content))

print("Bye Bro")

