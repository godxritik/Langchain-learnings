from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import dotenv

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt1 = PromptTemplate(
    template="Write a detailed 300 words article on {topic}.",
    input_variables= ["topic"]
)

prompt2 = PromptTemplate(
    template="write a Title (only a single title) and 5 point summary for the article attached below:\n\n{article}",
    input_variables= ["article"],
)

parser = StrOutputParser()

#passing the prompt into model and extracting it, then passing it to model again !!
chain = prompt1 | model | parser | prompt2 | model | parser

article_title = chain.invoke({"topic" : "Black Holes"})

print(article_title)

