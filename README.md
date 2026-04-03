# 🏥 Hospital RAG-based Question Answering System

## 📌 Overview

This project implements a Retrieval-Augmented Generation (RAG) system that answers user queries based on a hospital document (PDF). It retrieves relevant information and generates accurate responses using an LLM.

---

## 🧠 Architecture

1. **Document Ingestion**

   * Load hospital PDF
   * Convert text into chunks

2. **Embedding Generation**

   * Use Sentence Transformers to convert text into vectors

3. **Vector Storage**

   * Store embeddings in Supabase vector database

4. **Query Processing**

   * Convert user query into embedding
   * Perform similarity search

5. **Response Generation**

   * Pass retrieved context to Groq LLM
   * Generate final answer

---

## ⚙️ Setup Steps

1. Clone the repository:

   ```
   git clone <your-repo-link>
   cd hospital_rag_project
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Add API keys:

   * Supabase URL & Key
   * Groq API Key

4. Run backend:

   ```
   python -m uvicorn main:app --reload
   ```

5. Ingest data:
   Open:

   ```
   http://127.0.0.1:8000/ingest
   ```

6. Run frontend:

   ```
   streamlit run app.py
   ```

---

## 💬 Sample Queries

* What is emergency number?
* What services does the hospital provide?
* What is the ambulance contact?
* What are OPD timings?

---

## ✅ Output

The system retrieves relevant document chunks and generates accurate answers using AI.

---

## 🚀 Tech Stack

* FastAPI
* Streamlit
* Sentence Transformers
* Supabase (Vector DB)
* Groq LLM
