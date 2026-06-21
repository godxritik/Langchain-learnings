from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os

# reading files to generate embeddings
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

# setting up the model
model = SentenceTransformer("BAAI/bge-m3")


doc_embeddings = model.encode_document(doc_texts)
query_embedding = model.encode("which company owns a messaging software?")

# print(query_embedding)
# print(doc_embeddings)

scores = cosine_similarity([query_embedding],doc_embeddings)

print(scores.shape)

print(list(enumerate(scores[0])))

sorted_scores = sorted(list(enumerate(scores[0])), key=lambda x:x[1], reverse=True)
highest_similarity_index, highest_similarity_score = sorted_scores[0]

print(f"Highest similarity document: {documents[highest_similarity_index]['filename']}")
print(f"Content: {documents[highest_similarity_index]['content']}")
print(f"Similarity Score: {highest_similarity_score}")
