from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv
dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

output = model.invoke("write a java program that check whether a number is prime or not, just output the code, no explanation")
print(output.content)

with open("response.txt","a", encoding="utf-8") as file:
    file.write(str(output.content))
