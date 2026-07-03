from langchain_openai import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

embedding_model = OpenAIEmbeddings(
    model="text-embedding-bge-m3",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    check_embedding_ctx_length=False
)

print("model created")

splitter = SemanticChunker(
    embeddings=embedding_model,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

print("splitter created")

file_text = ""
with open("robotics.txt", "r") as file:
    file_text += file.read()
 
print("file loaded")

docs = splitter.create_documents([file_text])

for doc in docs:
    print(doc)



