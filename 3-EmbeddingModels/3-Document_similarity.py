from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()

directory = "tech_companies"

documents = []

# Read all text files
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            documents.append(
                {
                    "filename": filename,
                    "content": file.read().strip()
                }
            )

print(f"Total documents loaded: {len(documents)}")

# Extract text content only
doc_texts = [doc["content"] for doc in documents]

# Create embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    output_dimensionality=3072
)

query = "which company owns a messaging software"

# Generate document embeddings
doc_embeddings = np.array(
    embeddings.embed_documents(doc_texts)
)

# Generate query embedding
query_embedding = np.array(
    embeddings.embed_query(query)
).reshape(1, -1)

# Compute cosine similarity
scores = cosine_similarity(
    query_embedding,
    doc_embeddings
)

print("\nSimilarity Scores:")
print("-" * 50)

for i, score in enumerate(scores[0]):
    print(f"{documents[i]['filename']} : {score:.4f}")

# Top K Results
top_k = 3

top_indices = np.argsort(scores[0])[::-1][:top_k]

print("\nTop Matches:")
print("-" * 50)

for rank, idx in enumerate(top_indices, start=1):
    print(f"\nRank #{rank}")
    print(f"File: {documents[idx]['filename']}")
    print(f"Similarity Score: {scores[0][idx]:.4f}")

    preview = documents[idx]["content"][:200]
    print(f"Preview: {preview}...")

# Best Match
best_idx = top_indices[0]

print("\nBest Match:")
print("-" * 50)
print(f"File: {documents[best_idx]['filename']}")
print(f"Score: {scores[0][best_idx]:.4f}")

print("\nFull Content:")
print(documents[best_idx]["content"])