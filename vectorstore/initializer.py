from pathlib import Path

from vectorstore.create_vectorstore import create_vectorstore


VECTORSTORE_PATH = Path("vectorstore/chroma_db")


def initialize_vectorstore():
    if VECTORSTORE_PATH.exists():
        print("ChromaDB already exists.")
        return

    print("ChromaDB not found. Creating vector store...")

    create_vectorstore()

    print("ChromaDB created successfully.")