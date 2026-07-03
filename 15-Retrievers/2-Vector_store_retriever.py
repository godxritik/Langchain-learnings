from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

embedding_model = OpenAIEmbeddings(
    model="text-embedding-bge-m3",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    check_embedding_ctx_length=False
)

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()
print((len(docs)))

print(type(docs))

vector_store = Chroma.from_documents(
    documents=docs,
    # persist_directory="chroma_db",
    embedding=embedding_model,
    collection_name="AI-books"
)

retriever = vector_store.as_retriever()

query = "what book talks about Deep learning?"

result = retriever.invoke(query)

print(len(result))
print(type(result))
print(result)

