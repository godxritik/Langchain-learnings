from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio",
    model="qwen2.5-coder-3b-instruct@q4_k_m",
    temperature=1.5
)

parser = StrOutputParser()

tweet_generate_prompt = PromptTemplate(
    template="Generate a twitter tweet about {topic}",
    input_variables=["topic"]
)

linkedinPost_generate_prompt = PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=["topic"]
)

# RunnableParallel returns a dictionary representing the result of all the chains
chain = RunnableParallel({
    "tweet": RunnableSequence(tweet_generate_prompt, model, parser),
    "linkedin_post": RunnableSequence(tweet_generate_prompt, model, parser)
})

result = chain.invoke({"topic": "I have completed an internship at EPAM Systems Hyderabad at the role of software test automation engineer."})

print(result)