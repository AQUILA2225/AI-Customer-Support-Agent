import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

def get_embeddings():
    api_key = os.getenv("GOOGLE_API_KEY")
    model = os.getenv(
        "GOOGLE_EMBEDDING_MODEL",
        "models/gemini-embedding-001"
    )

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is missing from environment variables."
        )

    return GoogleGenerativeAIEmbeddings(
        model=model,
        google_api_key=api_key
    )