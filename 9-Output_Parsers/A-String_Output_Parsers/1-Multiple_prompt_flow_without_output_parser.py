from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)


prompt1 = PromptTemplate(
    template="Write a detailed 300 words article on {topic}.",
    input_variables= ["topic"]
)
prompt1 = prompt1.invoke({"topic" : "Constitution of India"})

prompt2 = PromptTemplate(
    template="write a Title (only a single title) for the article attached below:\n\n{article}",
    input_variables= ["article"],
)

article = model.invoke(prompt1)

prompt2 = prompt2.invoke({"article" : article})

final_result = model.invoke(prompt2)

print(final_result.content)