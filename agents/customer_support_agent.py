from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    ToolMessage
)

from llm.ollama_llm import get_llm
from tools.order_tracking import get_order_status
from tools.rag_policy_tool import search_company_policy


def run_customer_support_agent(user_query: str):

    llm = get_llm()

    tools = [
        get_order_status,
        search_company_policy
    ]

    llm_with_tools = llm.bind_tools(tools)

    tools_by_name = {
        tool.name: tool
        for tool in tools
    }

    messages = [
        SystemMessage(
            content="""
You are a helpful AI customer support assistant.

Use the available tools when needed.

Use get_order_status when the customer asks about:
- A specific order
- Order status
- Order tracking
- Shipping status
- Estimated delivery

Use search_company_policy when the customer asks about:
- Returns
- Refunds
- Cancellation rules
- Shipping policies
- Payment policies

After receiving information from a tool, provide a clear,
friendly, and concise answer.

Do not make up order information or company policies.
"""
        ),
        HumanMessage(content=user_query)
    ]

    # First LLM call
    response = llm_with_tools.invoke(messages)

    # Add the AI response to the conversation
    messages.append(response)

    # Check whether the LLM requested any tools
    if response.tool_calls:

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            selected_tool = tools_by_name[tool_name]

            # Execute the selected tool
            tool_result = selected_tool.invoke(tool_args)

            # Add tool result to conversation
            messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call["id"]
                )
            )

        # Send tool result back to LLM
        final_response = llm_with_tools.invoke(messages)

        return final_response.content

    # If no tool was required
    return response.content


if __name__ == "__main__":

    query = "Can i return a product after 20 days?"

    response = run_customer_support_agent(query)

    print("\nUser Question:")
    print(query)

    print("\nAI Assistant:")
    print(response)