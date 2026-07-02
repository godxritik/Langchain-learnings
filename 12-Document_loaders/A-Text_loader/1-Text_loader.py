from langchain_classic.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-coder-3b-instruct@q4_k_m",
    temperature=0
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template="Write a 5 pointer summary of the following text : {text}",
    input_variables=["text"]
)

loader = TextLoader("robotics.txt", encoding="utf-8")
docs = loader.load()

chain = prompt | model | parser
result = chain.invoke({"text" : docs[0].page_content})

print(result)


