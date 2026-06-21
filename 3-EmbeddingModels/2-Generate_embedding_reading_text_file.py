from langchain_google_genai import GoogleGenerativeAIEmbeddings
import dotenv
dotenv.load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", output_dimensionality=1536)

lines = []

with open("resources.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            lines.append(line)

print("lines content to embeddings:", lines)

vectors = embeddings.embed_documents(lines)

print(vectors)