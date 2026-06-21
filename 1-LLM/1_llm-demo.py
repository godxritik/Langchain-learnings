import langchain_google_genai
import dotenv

dotenv.load_dotenv()

llm = langchain_google_genai.GoogleGenerativeAI(model="gemini-2.5-flash", temperature=0, max_output_tokens=10000)

output = llm.invoke("Why america is a hypocrite country?")
print(output)

with open("response.txt", "w", encoding="utf-8") as file:
    file.write(output)











