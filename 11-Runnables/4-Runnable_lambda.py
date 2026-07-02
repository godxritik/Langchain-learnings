from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-coder-3b-instruct@q4_k_m",
    temperature=1
)

parser = StrOutputParser()

def word_counter(text):
    return len(text.split())

joke_generation_prompt = PromptTemplate(
    template="Generate a joke on the {topic}",
    input_variables=["topic"]
)

joke_explanation_prompt = PromptTemplate(
    template="Explain the given joke : {joke}",
    input_variables=["joke"]
)

joke_generation_chain = RunnableSequence(joke_generation_prompt, model, parser)

intermediate_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    "joke_explanation" : RunnableSequence(joke_explanation_prompt, model, parser),
    "word_count" : RunnableLambda(word_counter)
})

final_chain = RunnableSequence(joke_generation_chain, intermediate_chain)

result = final_chain.invoke({"topic" : "Artificial Intelligence"})

print("*** Joke *** \n", result["joke"])
print("--- joke explanation --- \n", result["joke_explanation"])
print("Word count : ", result["word_count"])

