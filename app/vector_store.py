# The following imports may fail if langchain is not installed.
try:
    from langchain.vectorstores import FAISS  # or Chroma
    from langchain.embeddings import HuggingFaceEmbeddings
except ImportError:
    FAISS = None
    HuggingFaceEmbeddings = None
    # Optionally, log or print a warning here

from typing import List

# Initialize embedding model (can use sentence-transformers or other supported models)
if HuggingFaceEmbeddings:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
else:
    embeddings = None

# Example: Store text chunks in FAISS

def create_faiss_vector_store(text_chunks: List[str]):
    if not FAISS or not embeddings:
        raise ImportError("LangChain or its dependencies are not installed.")
    return FAISS.from_texts(text_chunks, embeddings)

# Example: Retrieve similar chunks

def search_faiss_vector_store(vector_store, query: str, k: int = 5):
    if not vector_store:
        raise ValueError("Vector store is not initialized.")
    return vector_store.similarity_search(query, k=k)

