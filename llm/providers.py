import os
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    provider = os.getenv(
        "LLM_PROVIDER",
        "ollama"
    ).lower()

    if provider == "ollama":

        from langchain_ollama import ChatOllama
        model_name = os.getenv(
            "OLLAMA_MODEL",
            "llama3.2"
        )

        return ChatOllama(
            model=model_name,
            temperature=0
        )

    elif provider == "google":
        from langchain_google_genai import ChatGoogleGenerativeAI
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY is missing from the .env file."
            )

        model_name = os.getenv(
            "GOOGLE_MODEL",
            "gemini-2.5-flash"
        )

        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=0
        )

    else:
        raise ValueError(
            f"Unsupported LLM provider: {provider}"
        )
        
        