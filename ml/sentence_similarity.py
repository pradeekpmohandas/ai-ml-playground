from sentence_transformers import SentenceTransformer
import numpy as np

# Load the model (downloads automatically on first run)
model = SentenceTransformer('all-MiniLM-L6-v2')

# TechCorp test sentences
sentences = [
    "Dogs are allowed in the office on Fridays",
    "Pets can come to work on Furry Fridays",
    "Remote work policy allows 3 days from home"
]

# Embed all sentences at once
embeddings = model.encode(sentences)

# Cosine similarity using dot product
# (works correctly because SentenceTransformer normalizes vectors by default)
sim_1_2 = np.dot(embeddings[0], embeddings[1])
sim_1_3 = np.dot(embeddings[0], embeddings[2])
sim_2_3 = np.dot(embeddings[1], embeddings[2])

print(f"Dogs vs Pets:   {sim_1_2 * 100:.1f}% similar")
print(f"Dogs vs Remote: {sim_1_3 * 100:.1f}% similar")
print(f"Pets vs Remote: {sim_2_3 * 100:.1f}% similar")