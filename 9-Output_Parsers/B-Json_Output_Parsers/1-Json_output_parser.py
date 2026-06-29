from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import dotenv

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

#this output parser can parse the json output returned by the LLM
parser = JsonOutputParser()

template_1 = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n **try to keep the name Indian** \n {format_instructions}",
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = template_1 | model | parser
result = chain.invoke({})

print(result)
