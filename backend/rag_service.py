from llm.providers import get_llm
from tools.rag_policy_tool import search_company_policy


def answer_policy_question(question: str) -> str:
    # Retrieve relevant policy information
    policy_context = search_company_policy(question)

    # Get the LLM
    llm = get_llm()

    prompt = f"""
You are a helpful customer support assistant.

Answer the customer's question using ONLY the company policy
information provided below.

If the answer is not available in the provided policy information,
say that you do not have enough information.

Company Policy Information:
{policy_context}

Customer Question:
{question}

Provide a clear and helpful answer.
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":
    question = "Can I return a product after 20 days?"

    answer = answer_policy_question(question)

    print("\nCustomer Question:")
    print(question)

    print("\nAI Answer:")
    print(answer)