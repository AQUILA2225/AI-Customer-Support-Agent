from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_documents():
    with open(
        "data/company_policies.txt",
        "r",
        encoding="utf-8"
    ) as file:
        text = file.read()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(text)
    return chunks

if __name__ == "__main__":
    chunks = load_and_split_documents()

    print(f"Total chunks: {len(chunks)}\n")

    for index, chunk in enumerate(chunks, start=1):
        print(f"--- Chunk {index} ---")
        print(chunk)
        print()