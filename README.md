# CUDA Agentic Chatbot 🚀

This project is an agentic AI chatbot powered by a CUDA-accelerated LLM backend using FastAPI and a Next.js frontend.

## Key Features:
- CUDA-powered LLM inference
- FastAPI backend with agentic LangChain integration
- Next.js frontend for real-time chat UI
- GPU Docker orchestration via Docker Compose

### Upcoming:
- Triton Inference Server support
- GPU-based vector retrieval (FAISS)

---

## Project Structure:
- `/apps/web`: Chat UI (Next.js)
- `/apps/agents`: Backend API (FastAPI, CUDA)
- `/docker`: GPU Dockerfiles
- `/triton`: Triton model serving
- `/scripts`: CUDA environment setup
- `/docs`: Setup and usage documentation
