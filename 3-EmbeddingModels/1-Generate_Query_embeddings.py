from langchain_google_genai import GoogleGenerativeAIEmbeddings
import dotenv

dotenv.load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001", output_dimensionality=1536)

# embed single line
# query_vector = embeddings.embed_query("who is president DR Congo ?")

# @embedding multiple documents
docs = [
        "Honey never spoils; edible honey has been found in ancient tombs.",
        "Octopuses have three hearts and blue blood.",
        "Bananas are berries, but strawberries are not.",
        "A day on Venus is longer than a year on Venus.",
        "There are more possible chess games than atoms in the observable universe.",
        "Sharks existed before trees appeared on Earth."
        ]

query_vector = embeddings.embed_documents(docs)
print(query_vector)
