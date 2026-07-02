from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-coder-3b-instruct@q4_k_m",
    temperature=0
)

essay_generation_prompt = PromptTemplate(
    template="Write a long essay on the topic : {topic}",
    input_variables=["topic"]
)

summarization_prompt = PromptTemplate(
    template="Summarize the given essay : {essay}",
    input_variables=["essay"]
)

parser = StrOutputParser()

def printer(text):
    print(text.content)
    return text

essay_generation_chain = RunnableSequence(essay_generation_prompt, model, parser)

branching_chain = RunnableBranch(
    (lambda x: len(x.split()) > 200, RunnableSequence(summarization_prompt, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(essay_generation_chain, branching_chain)

result = final_chain.invoke({"topic" : "Russia vs USA"})

print(result)






