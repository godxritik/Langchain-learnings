from langchain_core.runnables import RunnableParallel
from langchain_openai import ChatOpenAI
from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import dotenv

dotenv.load_dotenv()

local_qwen_model = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-coder-3b-instruct@q4_k_m",
    temperature=0
)

gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

parser = StrOutputParser()

file_content = ""

with open("text_content.txt","r") as f:
    file_content = f.readlines()


prompt_notes = PromptTemplate(
    template="Generate well structured notes that i can use to study from the content below \n {text_content}",
    input_variables=["text_content"]
)

prompt_quiz = PromptTemplate(
    template="generate a 10 mcqs based questions for quiz from the content below (each mcq must have exactly 4 options). \n {text_content}",
    input_variables=["text_content"]
)

prompt_merge = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n Notes : {notes}, Quiz : {quiz}",
    input_variables=["notes", "quiz"]
)


parallel_chain = RunnableParallel({
    "notes" : prompt_notes | local_qwen_model | parser,
    "quiz" : prompt_quiz | local_qwen_model | parser
})

marge_chain = prompt_merge | local_qwen_model | parser

chain = parallel_chain | marge_chain

# result = chain.invoke({"text_content" : file_content})
for chunk in chain.stream({"text_content" : file_content}):
    print(chunk, end="")

# print(result)

chain.get_graph().print_ascii()