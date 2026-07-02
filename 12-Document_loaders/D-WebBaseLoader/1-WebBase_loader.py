from langchain_classic.document_loaders import WebBaseLoader

# this loader is used to load content from a url or a list of multiple urls

url = "https://docs.langchain.com/"
loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)
print(len(docs))

