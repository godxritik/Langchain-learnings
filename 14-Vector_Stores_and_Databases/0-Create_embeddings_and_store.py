from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# creating embedding_model instance
embedding_model = OpenAIEmbeddings(
    model="text-embedding-bge-m3",
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    check_embedding_ctx_length=False
)

# creating loader to load all the files inside a diretory
document_loader = DirectoryLoader(
    path="text_docs",
    glob="*.txt",
    loader_cls=TextLoader,
    use_multithreading=True
)

#loading files
text_docs = document_loader.load()

# creating vector store instance
vector_store = Chroma(
    embedding_function=embedding_model,
    persist_directory="chroma_db",
    collection_name="testing_chroma_db"
)

# storing documents into vector store
vector_store.add_documents(text_docs)

# fetching docs form store
res = vector_store.get(include=["embeddings", "documents", "metadatas"])

# perform similarity search on vector store
doc = vector_store.similarity_search(
    query="Which device is portable device",
    k=2
)

print(type(doc))
print(doc)

