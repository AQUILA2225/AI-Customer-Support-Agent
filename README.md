# 🤖 AI Customer Support Bot with Live Order Tracking

An AI-powered customer support application that combines **RAG (Retrieval-Augmented Generation)** with **AI tool calling** to answer company policy questions and provide live order tracking.

The agent intelligently decides whether to search the company policy knowledge base or call the order tracking tool based on the customer's query.

---

## 🚀 Live Demo

### Frontend
> https://ai-customer-support-agent-bot.streamlit.app/

### Backend API
https://ai-customer-support-agent-hag2.onrender.com

### API Documentation
https://ai-customer-support-agent-hag2.onrender.com/docs

---

# ✨ Features

- 🤖 AI-powered customer support assistant
- 📦 Live order tracking using Order ID
- 🔎 RAG-based company policy search
- 🧠 Semantic search using ChromaDB
- 🛠️ AI tool/function calling
- 📄 Support for:
  - Returns
  - Refunds
  - Shipping policies
  - Order cancellations
  - Payment policies
- ⚡ FastAPI REST API backend
- 💬 Interactive Streamlit chat interface
- 🗄️ SQLite order database
- 🔐 Environment variable configuration
- ☁️ Cloud deployment

---

# 🏗️ System Architecture

```text
                    ┌──────────────────┐
                    │       User       │
                    └────────┬─────────┘
                             │
                             ▼
                 ┌──────────────────────┐
                 │  Streamlit Frontend  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   FastAPI Backend    │
                 └──────────┬───────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │ AI Customer Support Agent   │
              └──────────────┬──────────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
   ┌────────────────────┐      ┌─────────────────────┐
   │ Order Tracking Tool│      │  RAG Policy Tool    │
   └─────────┬──────────┘      └──────────┬──────────┘
             │                            │
             ▼                            ▼
      ┌─────────────┐              ┌─────────────┐
      │   SQLite    │              │  ChromaDB   │
      └──────┬──────┘              └──────┬──────┘
             │                            │
             └─────────────┬──────────────┘
                           │
                           ▼
                  ┌────────────────┐
                  │   Gemini LLM   │
                  └────────┬───────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │  Final Response  │
                 └──────────────────┘
```

---

# 🧠 How the AI Agent Works

The application uses an AI agent with access to multiple tools.

When a customer sends a message, the agent analyzes the request and decides whether a tool is required.

```text
Customer Query
      │
      ▼
 Gemini LLM
      │
      ├── Order-related question
      │        │
      │        ▼
      │   get_order_status()
      │        │
      │        ▼
      │      SQLite
      │
      └── Policy-related question
               │
               ▼
      search_company_policy()
               │
               ▼
            ChromaDB
               │
               ▼
        Relevant Policy Context
               │
               ▼
           Gemini LLM
               │
               ▼
        Customer-Friendly Answer
```

---

# 📦 Order Tracking Workflow

When a customer asks:

```text
Where is my order ORD1001?
```

The agent follows this workflow:

1. The user sends an order-related query.
2. The Gemini model detects that order information is required.
3. The agent calls the `get_order_status` tool.
4. The tool queries the SQLite database.
5. Order details are returned to the agent.
6. The tool result is sent back to the LLM.
7. The LLM generates a customer-friendly response.

Example:

```text
User
  ↓
"Where is my order ORD1001?"
  ↓
AI Agent
  ↓
get_order_status(order_id="ORD1001")
  ↓
SQLite Database
  ↓
Order Status + Estimated Delivery
  ↓
Gemini
  ↓
Final Response
```

---

# 🔎 RAG Policy Search Workflow

When a customer asks:

```text
Can I return a product after 20 days?
```

The application follows this workflow:

1. Company policy documents are loaded.
2. Documents are split into smaller chunks.
3. Text embeddings are generated.
4. The chunks are stored in ChromaDB.
5. The user's question is converted into an embedding.
6. ChromaDB performs semantic similarity search.
7. Relevant policy information is retrieved.
8. The retrieved context is provided to the AI agent.
9. Gemini generates the final answer.

```text
Company Policies
       │
       ▼
Document Loader
       │
       ▼
Text Splitter
       │
       ▼
Google Embeddings
       │
       ▼
ChromaDB Vector Database
       │
       ▼
Similarity Search
       │
       ▼
Relevant Policy Context
       │
       ▼
Gemini LLM
       │
       ▼
Final Answer
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend REST API |
| Streamlit | Interactive frontend |
| LangChain | AI agent and tool integration |
| Google Gemini | Large Language Model |
| Google Embeddings | Text embeddings |
| ChromaDB | Vector database |
| SQLite | Order tracking database |
| Pydantic | Request and response validation |
| Requests | Frontend-backend communication |
| Render | Backend deployment |
| Streamlit Community Cloud | Frontend deployment |

---

# 📁 Project Structure

```text
AI_Customer_Support_agent/
│
├── agents/
│   └── customer_support_agent.py
│
├── backend/
│   └── main.py
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
│   ├── embeddings.py
│   └── providers.py
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
│   └── chroma_db/
│
├── .streamlit/
│   └── config.toml
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Installation

## 1. Clone the Repository

```bash
git clone <your-repository-url>
cd AI_Customer_Support_agent
```

## 2. Create a Virtual Environment

```bash
python -m venv ai_CSA
```

### Windows

```bash
ai_CSA\Scripts\activate
```

### macOS/Linux

```bash
source ai_CSA/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key

LLM_PROVIDER=google

GOOGLE_MODEL=your_gemini_model

GOOGLE_EMBEDDING_MODEL=models/gemini-embedding-001

API_URL=http://127.0.0.1:8000/chat
```

> Never upload your `.env` file or API keys to GitHub.

---

# 🗄️ Initialize the Order Database

Run:

```bash
python database/init_db.py
```

This creates the SQLite database containing sample order information.

---

# 🧠 Create the Vector Database

Run:

```bash
python -m vectorstore.create_vectorstore
```

This process:

```text
company_policies.txt
        ↓
Document Loading
        ↓
Text Splitting
        ↓
Google Embeddings
        ↓
ChromaDB
```

---

# 🚀 Run the Backend

Start the FastAPI server:

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Open the API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 💬 Run the Frontend

Open another terminal and run:

```bash
streamlit run frontend/app.py
```

The Streamlit application will open in your browser.

---

# 🔌 API Usage

## Chat Endpoint

### Endpoint

```text
POST /chat
```

### Request

```json
{
  "message": "Where is my order ORD1001?"
}
```

### Example Response

```json
{
  "response": "Your order ORD1001 is currently being processed and will be delivered soon."
}
```

---

# 🧪 Example Queries

### Order Tracking

```text
Where is my order ORD1001?
```

```text
What is the delivery status of ORD1002?
```

### Return Policy

```text
Can I return a product after 20 days?
```

### Refund Policy

```text
What is your refund policy?
```

### Shipping Policy

```text
What are your shipping policies?
```

### Payment Policy

```text
Which payment methods do you accept?
```

---

# ☁️ Deployment

The application uses a distributed deployment architecture.

```text
                 ┌─────────────────────────┐
                 │ Streamlit Community Cloud│
                 │        Frontend          │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │     Render Cloud        │
                 │    FastAPI Backend      │
                 └────────────┬────────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │   AI Support Agent     │
                  └────────────┬───────────┘
                               │
               ┌───────────────┴───────────────┐
               │                               │
               ▼                               ▼
         SQLite Database                  ChromaDB
               │                               │
               └───────────────┬───────────────┘
                               │
                               ▼
                         Google Gemini
```

### Backend Deployment

The FastAPI backend is deployed on Render.

### Frontend Deployment

The Streamlit application is deployed using Streamlit Community Cloud.

The frontend communicates with the backend using:

```env
API_URL=https://your-render-backend-url/chat
```

---

# 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Google Gemini API key |
| `LLM_PROVIDER` | LLM provider configuration |
| `GOOGLE_MODEL` | Gemini model used by the application |
| `GOOGLE_EMBEDDING_MODEL` | Model used for embeddings |
| `API_URL` | FastAPI backend chat endpoint |

---

# 🧩 Key Concepts Demonstrated

This project demonstrates several important AI engineering concepts:

- AI Agents
- Tool Calling
- Function Calling
- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- Vector Databases
- FastAPI REST APIs
- Streamlit Applications
- Environment Variable Management
- Cloud Deployment
- Frontend and Backend Integration
- SQLite Database Integration
- API Error Handling

---

# 🔮 Future Improvements

Possible improvements include:

- 🧠 Conversation memory
- 👤 User authentication
- 🐘 PostgreSQL database
- 📊 Admin dashboard
- 🐳 Docker containerization
- 📦 Real-time shipping API integration
- 👨‍💻 Human support escalation
- 📚 Multiple company knowledge documents
- ❌ Order cancellation functionality
- 📈 Monitoring and observability
- 🧪 Agent evaluation and testing
- 🔐 Role-based access control
- 💾 Persistent conversation history

---

# 📚 What I Learned

While building this project, I gained hands-on experience with:

- Building AI-powered applications
- Designing an AI agent with multiple tools
- Implementing RAG pipelines
- Working with ChromaDB
- Creating embeddings
- Integrating Google Gemini with LangChain
- Implementing function/tool calling
- Building REST APIs using FastAPI
- Creating interactive interfaces with Streamlit
- Working with SQLite databases
- Managing environment variables securely
- Debugging deployment issues
- Deploying AI applications to the cloud

---

# 👨‍💻 Author

**Bhaarathi Valluri**

Aspiring Python / AI Developer

---

## ⭐ If You Found This Project Useful

Consider giving the repository a **star ⭐**!