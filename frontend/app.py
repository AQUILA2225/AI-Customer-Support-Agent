import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/chat"


st.set_page_config(
    page_title="AI Customer Support",
    page_icon="🤖"
)

st.title("🤖 AI Customer Support Assistant")

st.write(
    "Ask me about your orders, returns, refunds, shipping, "
    "cancellations, or payment policies."
)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Get user input
if prompt := st.chat_input("Ask your question..."):

    # Store and display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)

    # Call FastAPI backend
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"message": prompt}
                )

                response.raise_for_status()

                answer = response.json()["response"]

                st.write(answer)

                # Store assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except requests.exceptions.ConnectionError:

                error_message = (
                    "Unable to connect to the backend. "
                    "Please make sure FastAPI is running."
                )

                st.error(error_message)

            except Exception as error:
                st.error(f"Something went wrong: {error}")