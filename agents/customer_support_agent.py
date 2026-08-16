from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    ToolMessage
)

from llm.providers import get_llm
from tools.order_tracking import get_order_status
from tools.rag_policy_tool import search_company_policy


def run_customer_support_agent(user_query: str) -> str:

    # Get the LLM
    llm = get_llm()

    # Available tools
    tools = [
        get_order_status,
        search_company_policy
    ]

    # Bind tools only for the first LLM call
    llm_with_tools = llm.bind_tools(tools)

    # Create a dictionary for tool lookup
    tools_by_name = {
        tool.name: tool
        for tool in tools
    }

    # Initial conversation
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

Do not make up order information or company policies.

After receiving information from a tool, provide a clear,
friendly, and concise answer to the customer.
"""
        ),
        HumanMessage(content=user_query)
    ]

    # First LLM call WITH tools
    response = llm_with_tools.invoke(messages)

    # Add AI response to conversation
    messages.append(response)

    # Check if the LLM requested a tool
    if response.tool_calls:

        # Execute all requested tools
        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            selected_tool = tools_by_name.get(tool_name)

            if selected_tool is None:
                tool_result = f"Tool '{tool_name}' is not available."
            else:
                try:
                    tool_result = selected_tool.invoke(tool_args)
                except Exception as e:
                    tool_result = f"Error while executing tool: {str(e)}"

            # Add tool result to conversation
            messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call["id"]
                )
            )

        # This forces the model to generate the final answer
        final_response = llm.invoke(messages)

        # Handle possible list/empty content safely
        if isinstance(final_response.content, str):
            return final_response.content

        if isinstance(final_response.content, list):
            text_parts = []

            for item in final_response.content:
                if isinstance(item, str):
                    text_parts.append(item)

                elif isinstance(item, dict):
                    if "text" in item:
                        text_parts.append(str(item["text"]))

            if text_parts:
                return " ".join(text_parts)

        return "I found the information, but I was unable to generate a response."


    # If no tool was required
    if isinstance(response.content, str):
        return response.content

    if isinstance(response.content, list):
        text_parts = []

        for item in response.content:
            if isinstance(item, str):
                text_parts.append(item)

            elif isinstance(item, dict):
                if "text" in item:
                    text_parts.append(str(item["text"]))

        if text_parts:
            return " ".join(text_parts)

    return "I'm sorry, but I was unable to generate a response."


if __name__ == "__main__":

    query = "Where is my order ORD1001?"

    response = run_customer_support_agent(query)

    print("\nUser Question:")
    print(query)

    print("\nAI Assistant:")
    print(response)