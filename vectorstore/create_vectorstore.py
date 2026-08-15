from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from data.load_documents import load_and_split_documents


def create_vectorstore():
    chunks = load_and_split_documents()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="vectorstore/chroma_db"
    )

    print(f"Successfully stored {len(chunks)} chunks in ChromaDB.")

    return vectorstore


if __name__ == "__main__":
    create_vectorstore()