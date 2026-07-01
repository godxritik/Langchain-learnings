from langchain_core.output_parsers import JsonOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import dotenv


dotenv.load_dotenv()

# using google gemini api
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=2)

# using local lm studio model - because api is slow
model = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-0.5b-instruct",
    temperature=0
)


parser = JsonOutputParser()

prompt1 = PromptTemplate(
    template="Write a detailed product review for {product}",
    input_variables=["product"]
)

prompt2 = PromptTemplate(
    template="extract the product review detail such as Product name, category, summary(strictly less than 20 words), sentiment(positive, negative, neutral) from the below  review \n {review} \n {format_instructions}",
    input_variables=["review"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

def printer(response):
    print(response.content)
    return response.content

chain = prompt1 | model | printer | prompt2 | model | parser
result =  chain.invoke({"product" : "samsung galaxy S26 ultra"})

print("*** OUTPUT ***")
print(result)
