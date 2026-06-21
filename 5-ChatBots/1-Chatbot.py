from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv

dotenv.load_dotenv()

chat_history = []

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1)

while True:
    user_input = input("You : ")
    if(user_input == "exit"):
        break
    chat_history.append(user_input)
    ai_response = model.invoke(user_input).content
    print("AI : ", ai_response)
    chat_history.append(ai_response)