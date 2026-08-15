# AI Customer Support Bot with Live Order Tracking

An AI-powered customer support application that answers company policy questions using Retrieval-Augmented Generation (RAG) and provides live order tracking using an SQLite database and AI tool calling.

## Features

- AI-powered customer support chatbot
- Live order tracking using Order ID
- RAG-based company policy search
- Semantic search using ChromaDB
- AI tool/function calling
- Return, refund, shipping, cancellation, and payment policy support
- FastAPI backend
- Streamlit chat interface
- Input validation and error handling

## Architecture

```text
User
  ↓
Streamlit Chat Interface
  ↓
FastAPI Backend
  ↓
AI Customer Support Agent
  │
  ├── Order Tracking Tool
  │       ↓
  │     SQLite
  │
  └── Policy Search Tool
          ↓
       ChromaDB
          ↓
      Policy Context
          ↓
       Ollama LLM
          ↓
     Final Response

```
## Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- Ollama
- Llama 3.2
- ChromaDB
- Sentence Transformers
- SQLite
- Pydantic

```
## Project Structure

ai_customer_support_agent/
│
├── agents/
│   └── customer_support_agent.py
│
├── backend/
│   ├── main.py
│   └── rag_service.py
│
├── data/
│   ├── company_policies.txt
│   └── load_documents.py
│
├── database/
│   ├── init_db.py
│   └── orders.db
│
├── frontend/
│   └── app.py
│
├── llm/
│   └── ollama_llm.py
│
├── models/
│   ├── chat.py
│   └── order.py
│
├── tools/
│   ├── order_tracking.py
│   └── rag_policy_tool.py
│
├── vectorstore/
│   ├── create_vectorstore.py
│   └── search_vectorstore.py
│
├── requirements.txt
├── .gitignore
└── README.md

```
## How It Works

Order Tracking

When a user asks about a specific order:

Where is my order ORD1001?

The AI agent:

- Detects that order information is required.
- Calls the get_order_status tool.
- Retrieves data from SQLite.
- Sends the tool result back to the LLM.
- Generates a customer-friendly response.
- Company Policy Questions

When a user asks:

Can I return a product after 20 days?

The AI agent:

- Detects that company policy information is required.
- Calls the search_company_policy tool.
- Searches ChromaDB using semantic similarity.
- Retrieves relevant policy information.
- Uses the LLM to generate a response.
  
Local Setup
1. Clone the repository
- git clone <your-repository-url>
- cd ai_customer_support_agent
2. Create a virtual environment
- python -m venv venv

Activate it.
Windows:
- venv\Scripts\activate
3. Install dependencies
- pip install -r requirements.txt
4. Create the vector database
- python vectorstore/create_vectorstore.py
5. Start Ollama

Make sure Ollama is running and the required model is available:

- ollama pull llama3.2
6. Start the FastAPI backend
- uvicorn backend.main:app --reload
7. Start the Streamlit application

Open another terminal and run:
- streamlit run frontend/app.py
  
```
## Future Improvements
```
- Conversation memory
- User authentication
- PostgreSQL database
- Admin dashboard
- Docker containerization
- Cloud deployment
- Multiple company documents
- Order cancellation functionality
- Human support escalation
