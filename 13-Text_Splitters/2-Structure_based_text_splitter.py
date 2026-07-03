from langchain_text_splitters import RecursiveCharacterTextSplitter

file_text = ""

with open("robotics.txt", "r") as file:
    file_text += file.read()

# print(file_text)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10
)

doc = splitter.split_text(file_text)

print(doc)
