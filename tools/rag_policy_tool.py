from langchain_core.tools import tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


@tool
def search_company_policy(query: str) -> str:
    """
    Search the company policy knowledge base for information about
    returns, refunds, shipping, cancellations, or payments.

    Use this tool when a customer asks about company policies,
    rules, refunds, returns, shipping policies, cancellations,
    or payment methods.
    """

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

    if not results:
        return "No relevant company policy information found."

    policy_context = "\n\n".join(
        document.page_content
        for document in results
    )

    return policy_context


if __name__ == "__main__":
    result = search_company_policy.invoke(
        {
            "query": "Can I return a product after 20 days?"
        }
    )

    print(result)