from datetime import time

from langchain_classic.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

# lazy_load() loads only one document at a time, saving both memory and load time
docs = loader.lazy_load()

for doc in docs:
    print(doc.metadata)
