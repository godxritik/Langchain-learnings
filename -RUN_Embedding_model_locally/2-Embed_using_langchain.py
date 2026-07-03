from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings(
    model="text-embedding-bge-m3",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    check_embedding_ctx_length=False
)

query = """
Origins of Robotics
The origins of robotics date back to the early 20th century with the development of the first industrial robots by George Devol and Joseph Engelberger. These machines were designed for repetitive tasks such as welding and drilling, marking the beginning of automated manufacturing. Over time, robotic technology has evolved into a complex field that encompasses everything from simple machines to highly sophisticated systems.
"""

vector = embedding_model.embed_query(query)

print(len(vector))  # 1024
print(vector)