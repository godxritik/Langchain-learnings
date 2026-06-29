from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema
import dotenv

dotenv.load_dotenv()

schema = [
    ResponseSchema(name="Fact-1", description="A fact about the fictional person"),
    ResponseSchema(name="Fact-2", description="A fact about the fictional person"),
    ResponseSchema(name="Fact-3", description="A fact about the fictional person"),
]

#using structure output parser help to enforce a schema in llm output
# ***LIMITATION*** this does not provide schema validation, data types of the output from llm cannot be fixed
parser = StructuredOutputParser.from_response_schemas(schema)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

prompt1 = PromptTemplate(
    template="Give three facts about the {topic} \n {format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

chain = prompt1 | model | parser
result = chain.invoke({"topic": "Black Holes"})

print(result)


