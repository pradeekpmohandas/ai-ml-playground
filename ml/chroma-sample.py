# Chroma Vector Database Example
import chromadb

# Setup - runs in memory, no server needed
# By default uses all-MiniLM-L6-v2 to auto embed your text
client = chromadb.Client()

collection = client.create_collection("policies")

# Add 3 policy documents (Chroma handles embeddings automatically)
policies = [
    "Dogs are allowed in the office on Fridays",
    "Pets can come to work on Furry Fridays",
    "Remote work policy allows 3 days from home"
]

for i, policy in enumerate(policies):
    collection.add(
        documents=[policy],
        ids=[f"policy_{i}"]
    )

# Query the system
query = "Can I bring my dog to work?"
results = collection.query(query_texts=[query], n_results=2)

# Show results
print("Query:", query)
print("\nTop matches:")
for doc, distance in zip(results["documents"][0], results["distances"][0]):
    print(f"  - {doc}")
    print(f"    distance: {distance:.4f}")