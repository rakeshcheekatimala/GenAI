import numpy as np

def batch_similarity_search(query_vector, embeddings, k=3):
    """
    Vectorized cosine similarity search using NumPy.
    
    query_vector: np.array of shape (d,)
    embeddings: list of (chunk_text, embedding_vector)
    """
    # Extract vectors and labels
    texts = [chunk for chunk, _ in embeddings]
    vectors = np.array([vector for _, vector in embeddings])  # shape: (n, d)

    # Normalize vectors (for cosine similarity)
    query_norm = query_vector / np.linalg.norm(query_vector)
    vectors_norm = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)

    # Compute cosine similarities in one go (dot products)
    similarities = np.dot(vectors_norm, query_norm)

    # Sort indices by similarity score
    top_k_indices = np.argsort(similarities)[::-1][:k]

    # Collect results
    results = [(texts[i], similarities[i]) for i in top_k_indices]
    return results


# ---------------- Example ----------------

# Fake embeddings
embeddings = [
    ("AI is transforming technology", np.array([1, 2, 3])),
    ("Leadership is evolving with AI", np.array([2, 1, 0])),
    ("Parenting and technology balance", np.array([0, 1, 1]))
]

# Query embedding
query_vector = np.array([1, 1, 2])

# Run batch similarity search
results = batch_similarity_search(query_vector, embeddings, k=2)

# Print results
for chunk, score in results:
    print(f"Chunk: {chunk}, Similarity: {score:.3f}")
