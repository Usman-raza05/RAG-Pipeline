from src.data_loader import load_all_documents
# from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch


# Example Usage

if __name__ == "__main__":
    # docs = load_all_documents("data")
    # chunks = EmbeddingPipeline().chunk_documents(docs)
    # chunkvectors = EmbeddingPipeline().embed_chunks(chunks)
    # print(chunkvectors)

    # store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    # store.load()
    # print(store.qyery("What is fellowshift backend?", top_k=3))

    rag_search = RAGSearch()
    query = "What is fellowshift backend?"
    summary = rag_search.search_and_summarized(query, top_k= 3)
    print("Summary:", summary)