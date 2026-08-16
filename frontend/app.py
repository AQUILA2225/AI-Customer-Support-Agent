import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/chat"
)

st.set_page_config(
    page_title="AI Customer Support",
    page_icon="🤖"
)
st.title("🤖 AI Customer Support Assistant")
st.write(
    "Ask me about your orders, returns, refunds, shipping, "
    "cancellations, or payment policies."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Ask your question..."):
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"message": prompt},
                    timeout=120
                )
                response.raise_for_status()
                data = response.json()
                answer = data.get(
                    "response",
                    "Sorry, I was unable to generate a response."
                )
                st.write(answer)
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )
            except requests.exceptions.ConnectionError:
                error_message = (
                    "Unable to connect to the AI backend. "
                    "Please try again later."
                )
                st.error(error_message)
            except requests.exceptions.Timeout:
                st.error(
                    "The request took too long. "
                    "Please try again."
                )
            except requests.exceptions.HTTPError as error:
                st.error(
                    f"Backend error: {error}"
                )
            except Exception as error:
                st.error(
                    f"Something went wrong: {error}"
                )