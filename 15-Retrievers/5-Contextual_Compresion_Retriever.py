from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor

chat_model = ChatOpenAI(
    base_url="http://127.0.0.1:1234/v1",
    model="qwen2.5-0.5b-instruct",
    api_key="lm-studio",
    temperature=0
)

embedding_model = OpenAIEmbeddings(
    base_url="http://127.0.0.1:1234/v1",
    model="text-embedding-bge-m3",
    api_key="lm-studio",
    check_embedding_ctx_length=False
)

document_loader = DirectoryLoader(
    path="text_docs",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = document_loader.load()
print("No. of documents loaded : ",len(documents))

vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name="article_texts"
)

base_retriever = vector_store.as_retriever(search_kwargs={"k":2})

compressor = LLMChainExtractor.from_llm(chat_model)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

query = "which device should i use for my project research?"

compressed_result = compression_retriever.invoke(query)

print(len(compressed_result))
print(type(compressed_result))

for doc in compressed_result:
    print(doc)


