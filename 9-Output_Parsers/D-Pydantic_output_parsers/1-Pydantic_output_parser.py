from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import dotenv

dotenv.load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

class Person(BaseModel):
    first_name:str = Field(description="First name of the person")
    last_name:str = Field(description="Last name of the person")
    age:int = Field(description="Age of the person", gt=18)
    gender:str = Field(description="Gender of the person")
    city:str = Field(description="City of the person")

parser = PydanticOutputParser(pydantic_object=Person)

prompt1 = PromptTemplate(
    template="Generate the first name, last name, age, gender, city of a fictional {nationality} person \n {format_instructions}",
    input_variables=["nationality"],
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain = prompt1 | model | parser

result = chain.invoke({"nationality": "African"})

print(result)



