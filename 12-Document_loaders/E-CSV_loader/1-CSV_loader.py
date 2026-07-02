from langchain_classic.document_loaders import CSVLoader

loader = CSVLoader(file_path="student_records.csv")

docs = loader.lazy_load()

for doc in docs:
    print(doc.page_content)



