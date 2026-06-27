from httptools.parser.parser import Optional
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated

model  = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",  # can be any value
    model="qwen2.5-0.5b-instruct",
    temperature=0
)

# this class represents the schema this called type dictionary
# we can also provide the llm with some hints by writing annotations, using annotated keyword
# we can also make any field optional using optional from typing library

# like Annotated[Optional[str], "brief summary of review"]
class Review(TypedDict):
    product_name: str
    summary: Annotated[str, "a brief summary of the review, not more than 20 words"]   #this is how to provide annotations
    sentiment: Annotated[str, "return the sentiment of the review, it may be positive, negative, mixed and neutral"]

structured_model = model.with_structured_output(Review)


response = structured_model.invoke("The iPhone 17 is a remarkable device, with stunning visuals and lightning-fast performance. It's perfect for both casual users and tech enthusiasts alike. The design is sleek and modern, and the camera quality is simply amazing. I'm impressed by how long it lasts on a single charge. The iPhone 17 has everything you need. Its powerful processor, great battery life, and impressive camera make it an outstanding choice for everyday use. Overall, a fantastic investment.")


print(response["product_name"])
print(response["summary"])
print(response["sentiment"])
