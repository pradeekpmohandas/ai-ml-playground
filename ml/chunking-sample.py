def chunk_document(text, chunk_size=500, overlap=50):
    """Split document into overlapping chunks"""
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        # Try to break at sentence boundary
        if end < len(text):
            last_period = chunk.rfind('.')
            if last_period > chunk_size * 0.7:  # period is in last 30% of chunk
                chunk = chunk[:last_period + 1]
                end = start + last_period + 1

        chunks.append(chunk.strip())
        start = end - overlap  # overlap for context

    return chunks


# ----------------------------
# Sample document
# ----------------------------
document = """
Dogs are allowed in the office on Fridays. This policy was introduced in 2023 after 
employee feedback showed that pet-friendly days improve morale. Employees must register 
their dogs with HR before bringing them in. All dogs must be vaccinated and well behaved.

Pets can come to work on Furry Fridays. The initiative started as a monthly event but 
became weekly due to its popularity. There is a designated pet area on the second floor. 
Food and water bowls are provided by the office. Employees are responsible for cleaning 
up after their pets at all times.

Remote work policy allows 3 days from home per week. Employees can choose which days 
they work remotely. Core hours are 10am to 3pm regardless of location. All remote 
workers must be available on Slack during core hours. Equipment requests for home 
offices must be submitted through the IT portal.
"""

# ----------------------------
# Run the chunker
# ----------------------------
chunks = chunk_document(document, chunk_size=200, overlap=30)

# ----------------------------
# Show results
# ----------------------------
print(f"Original document: {len(document)} characters")
print(f"Number of chunks:  {len(chunks)}")
print(f"Chunk size:        200 characters")
print(f"Overlap:           30 characters")
print("=" * 60)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1} ({len(chunk)} chars):")
    print("-" * 40)
    print(chunk)

# ----------------------------
# Show overlap in action
# ----------------------------
print("\n" + "=" * 60)
print("OVERLAP DEMONSTRATION")
print("=" * 60)
if len(chunks) >= 2:
    # find the overlapping text between chunk 1 and chunk 2
    end_of_chunk1 = chunks[0][-30:]
    start_of_chunk2 = chunks[1][:30]
    print(f"\nLast 30 chars of chunk 1: '...{end_of_chunk1}'")
    print(f"First 30 chars of chunk 2: '{start_of_chunk2}...'")
    print("\nNotice the overlap — context is preserved across boundaries")