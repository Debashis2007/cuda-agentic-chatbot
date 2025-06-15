from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Agentic AI Chatbot Backend is running"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")

    # Call gRPC CUDA server placeholder
    # In next commits, we will replace this with actual gRPC call
    grpc_response = requests.post("http://cuda-grpc-server:50051/infer", json={"input": user_input})

    return {"response": grpc_response.json().get("output", "No response from model.")}