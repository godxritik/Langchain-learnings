from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from networkx.algorithms import similarity

embedding_model = OpenAIEmbeddings(
    base_url="http://127.0.0.1:1234/v1",
    model="text-embedding-bge-m3",
    api_key="lm-studio",
    check_embedding_ctx_length=False
)

chat_model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    model="qwen2.5-0.5b-instruct",
    api_key="lm-studio",
    temperature=1
)

loader = DirectoryLoader(
    path="text_docs",
    glob="*.txt",
    loader_cls=TextLoader
)

docs = loader.load()

print("No. of docs loaded : ", len(docs))

#creating vector store instance from documents
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model
)

retriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(search_kwargs={"k":1}),
    llm=chat_model
)

query = "which device should i use for my project research?"

result = retriever.invoke(query)

print(len(result))
print(type(result))

for doc in result:
    print(doc)


