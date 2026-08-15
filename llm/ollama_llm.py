from langchain_ollama import ChatOllama


def get_llm():
    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    return llm


if __name__ == "__main__":
    llm = get_llm()

    response = llm.invoke(
        "Say hello as a customer support assistant in one sentence."
    )

    print(response.content)