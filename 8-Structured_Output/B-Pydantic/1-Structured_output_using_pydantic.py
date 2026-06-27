# from langchain_openai import  ChatOpenAI
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import Optional, Annotated, Literal
import dotenv

dotenv.load_dotenv()

model  = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


class Review(BaseModel):
    key_themes : list[str] = Field(description="key themes of the review")
    product_name : str = Field(description="product name")
    summary : str = Field(description="a brief summary of the review, not more than 20 words")
    sentiment : Literal["positive", "negative", "mixed", "neutral"] = Field(description="return the sentiment of the review, it may be positive, negative, mixed and neutral")
    pros : list[str] = Field(description="list of pros of the review")
    cons : list[str] = Field(description="list of cons of the review")


structured_model = model.with_structured_output(Review)
result = structured_model.invoke("The iPhone 17 is a remarkable device, with stunning visuals and lightning-fast performance. It's perfect for both casual users and tech enthusiasts alike. The design is sleek and modern, and the camera quality is simply amazing. I'm impressed by how long it lasts on a single charge. The iPhone 17 has everything you need. Its powerful processor, great battery life, and impressive camera make it an outstanding choice for everyday use. Overall, a fantastic investment.")


output_dict = dict(result)
print(output_dict["key_themes"])
print(output_dict["product_name"])
print(output_dict["summary"])

