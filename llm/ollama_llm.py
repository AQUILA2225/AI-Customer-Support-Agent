import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

def get_llm():
    model_name = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2"
    )

    llm = ChatOllama(
        model=model_name,
        temperature=0
    )
    return llm

if __name__ == "__main__":
    llm = get_llm()

    response = llm.invoke(
        "Say hello as a customer support assistant in one sentence."
    )
    print(response.content)