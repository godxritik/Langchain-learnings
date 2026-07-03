from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang="en")

query = "India"

docs = retriever.invoke(query)

print(type(docs))

for doc in docs:
    print(doc.page_content)

