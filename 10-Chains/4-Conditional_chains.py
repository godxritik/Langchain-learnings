from typing import Literal
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
import dotenv

dotenv.load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

#using local llm because the api limit is exhausted
model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    model="qwen2.5-coder-3b-instruct@q4_k_m",
    api_key="lm-studio",
    temperature=1
)

class Feedback(BaseModel):
    sentiment : Literal["positive", "negative", "neutral"] = Field(description="give the sentiment of the feedback")

string_parser = StrOutputParser()
feedback_parser = PydanticOutputParser(pydantic_object=Feedback)

classifier_prompt = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}",
    input_variables = ["feedback"],
    partial_variables={"format_instructions": feedback_parser.get_format_instructions()}
)

positive_feedback_response_prompt = PromptTemplate(
    template="Write an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)

negative_feedback_response_prompt = PromptTemplate(
    template="Write an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)

neutral_feedback_response_prompt = PromptTemplate(
    template="Write an appropriate response to this neutral feedback \n {feedback}",
    input_variables=["feedback"]
)

classification_chain = classifier_prompt | model | feedback_parser



# result = classification_chain.invoke({"feedback": "this is not a good phone nor bad, it is kind of okay"})
# print(result)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", positive_feedback_response_prompt | model | string_parser),
    (lambda x: x.sentiment == "negative", negative_feedback_response_prompt | model | string_parser),
    (lambda x: x.sentiment == "neutral", neutral_feedback_response_prompt | model | string_parser),
    RunnableLambda(lambda x: "Could not find the sentiment")
)

master_chain = classification_chain | branch_chain

# Testing positive chain
result = master_chain.invoke({"feedback" : "This is an amazing smartphone with a lots of features and only little downsides"})

# Testing negative chain
# result = master_chain.invoke({"feedback" : "This is the worst smartphone i have ever seen"})

# Testing neutral chain
# result = master_chain.invoke({"feedback" : "this is not a good phone nor bad, it is kind of okay"})

print(result)

master_chain.get_graph().print_ascii()

