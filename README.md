# 🧠 Retrieval-Augmented Generation (RAG) Based Chat Application

## 📌 Project Overview
1. This project implements a Retrieval-Augmented Generation (RAG) pipeline using LangChain, Chroma vector database, Hugging Face embeddings, and a Hugging Face LLM (FLAN-T5) to answer user queries from a custom knowledge base (any website).
2. This project demonstrates end-to-end RAG architecture, including document chunking, vector storage, semantic search with MMR, and controlled answer generation.

## 🚀 Features
📄 Document ingestion and preprocessing

✂️ Smart text chunking with overlap

🔢 Semantic embeddings using Hugging Face models

🗄️ Vector storage and retrieval using ChromaDB

🎯 Maximum Marginal Relevance (MMR) for diverse retrieval

🤖 Answer generation using Hugging Face LLM (FLAN-T5)

🔗 Modular RAG pipeline using LangChain

💬 Chat-style web interface (Flask)

## 🏗️ System Architecture
```text
User Query
   ↓
Chat UI (HTML + JS)
   ↓
Flask Backend
   ↓
LangChain RAG Pipeline
   ↓
MMR Retriever (Chroma Vector DB)
   ↓
Relevant Context
   ↓
HuggingFace LLM (Flan-T5)
   ↓
Answer Returned to Chat UI
```
## 🧩 Tech Stack
| Component          | Technology Used                    |
| ------------------ | ---------------------------------- |
| Language           | Python                             |
| Framework          | LangChain                          |
| Vector Database    | ChromaDB                           |
| Embeddings         | Hugging Face Sentence Transformers |
| LLM                | google/flan-t5-base                |
| Retrieval Strategy | MMR (Maximum Marginal Relevance)   |

## 📁 Project Structure
```text
rag/
│
├── app.py                 # Flask backend
├── project.py             # RAG pipeline logic
├── index_data.py          # One-time data indexing
│
├── templates/
│   └── chat.html          # Chat UI
│
├── static/
│   ├── style.css
│   └── chat.js
│
├── chroma_db/             # Persistent vector store
└── README.md
```
## ▶️ How to Run the Project
1️⃣ Index Website Data (Run Once)
```text
python index_data.py
```
2️⃣ Start Web Application
```text
python app.py
```
3️⃣ Open in Browser
```text
http://127.0.0.1:5000
```
