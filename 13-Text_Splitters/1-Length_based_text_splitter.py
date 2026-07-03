# This Splitter splits the text as per the number of characters
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=100,
    chunk_overlap=0
)

file_text = ""

with open("robotics.txt", "r") as file:
    file_text += file.read()

result = text_splitter.split_text(file_text)

print(result)


