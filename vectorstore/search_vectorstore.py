from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def search_policy(query: str):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory="vectorstore/chroma_db",
        embedding_function=embeddings
    )

    results = vectorstore.similarity_search(
        query,
        k=2
    )

    return results


if __name__ == "__main__":
    query = "Can I return a product after 20 days?"

    results = search_policy(query)

    print(f"\nQuestion: {query}\n")

    for index, document in enumerate(results, start=1):
        print(f"--- Result {index} ---")
        print(document.page_content)
        print()