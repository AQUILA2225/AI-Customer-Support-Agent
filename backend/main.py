import os
from vectorstore.create_vectorstore import create_vectorstore

from fastapi import FastAPI
from agents.customer_support_agent import run_customer_support_agent
from models.chat import ChatRequest, ChatResponse
from models.order import OrderResponse
from tools.order_tracking import get_order_status
from vectorstore.initializer import initialize_vectorstore
from fastapi import FastAPI, HTTPException



VECTORSTORE_PATH = "vectorstore/chroma_db"

if not os.path.exists(VECTORSTORE_PATH):
    print("ChromaDB not found. Creating vector database...")
    create_vectorstore()
else:
    print("ChromaDB found. Using existing vector database.")

app = FastAPI(
    title="AI Customer Support Agent",
    description="Backend API for an AI-powered customer support system",
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    initialize_vectorstore()

@app.get("/")
def home():
    return {
        "message": "AI Customer Support Agent API is running"
    }


@app.get(
    "/orders/{order_id}",
    response_model=OrderResponse
)
def track_order(order_id: str):

    result = get_order_status.invoke(
        {"order_id": order_id}
    )

    return result


@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    try:
        user_message = request.message.strip()

        if not user_message:
            raise HTTPException(
                status_code=400,
                detail="Message cannot be empty."
            )

        response = run_customer_support_agent(
            user_message
        )

        return ChatResponse(
            response=response
        )

    except HTTPException:
        raise

    except Exception as error:
        print(f"Chat error: {error}")

        raise HTTPException(
            status_code=500,
            detail="Unable to process your request. Please try again."
        )