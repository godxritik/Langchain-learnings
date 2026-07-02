from langchain_classic.document_loaders import PyPDFLoader

# this pyPDF loader is recommended only for textual pdfs not for scanned PDF files

loader = PyPDFLoader("Ritik_Gaur_Internship_Report.pdf")

docs = loader.load()

print(docs[19].page_content)
print(docs[19].metadata)

