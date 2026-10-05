from src.rag.data_loader import load_all_documents
from src.rag.embedding import EmbeddingPipeline
from src.rag.vectorstore import FaissVectorStore
from src.rag.search import RAGSearch


if __name__ == "__main__":
    data_path = r"C:\Users\Saif\Documents\RAG\data"
    documents = load_all_documents(data_path)

    chunks = EmbeddingPipeline().chunk_documents(documents)
    embeddings = EmbeddingPipeline().embed_chunks(chunks)
    print(embeddings)
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(documents)
    # store.load()
    # print(store.query("What is attention mechanism?", top_k=3))
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
