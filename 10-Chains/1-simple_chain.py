from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import dotenv

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt = PromptTemplate(
    template="Generate the name, city, age and gender of a fictional {nationality} person",
    input_variables=["nationality"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"nationality": "Indian"})

print(result)

#visualizing chains
chain.get_graph().print_ascii()

