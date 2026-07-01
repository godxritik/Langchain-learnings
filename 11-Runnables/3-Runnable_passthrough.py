from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-coder-3b-instruct@q4_k_m",
    temperature=1
)

parser = StrOutputParser()

joke_generate_prompt = PromptTemplate(
    template="Generate a joke on the {topic}",
    input_variables=["topic"]
)

joke_explanation_prompt = PromptTemplate(
    template="Explain the given joke : {joke}",
    input_variables=["joke"]
)


joke_generation_chain = RunnableSequence(joke_generate_prompt, model, parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "joke_explanation": RunnableSequence(joke_explanation_prompt, model, parser)
})

final_chain = RunnableSequence(joke_generation_chain, parallel_chain)

result = final_chain.invoke({"topic", "AI"})

print(result["joke"])
print(result["joke_explanation"])

