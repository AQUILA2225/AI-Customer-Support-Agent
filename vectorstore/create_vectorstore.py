from langchain_chroma import Chroma
from data.load_documents import load_and_split_documents
from llm.embeddings import get_embeddings

def create_vectorstore():
    chunks = load_and_split_documents()
    embeddings = get_embeddings()
    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        persist_directory="vectorstore/chroma_db"
    )
    print(f"Successfully stored {len(chunks)} chunks in ChromaDB.")
    return vectorstore

if __name__ == "__main__":
    create_vectorstore()
    