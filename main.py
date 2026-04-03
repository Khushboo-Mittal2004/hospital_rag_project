from fastapi import FastAPI
from pydantic import BaseModel
from ingest import load_pdf, chunk_text, get_embeddings
from db import store_chunks, search_similar
from sentence_transformers import SentenceTransformer
from rag import generate_answer

app = FastAPI()

model = SentenceTransformer('all-MiniLM-L6-v2')

class Query(BaseModel):
    question: str

# 🔥 RUN THIS ONLY ONCE (for ingestion)
@app.get("/ingest")
def ingest():
    try:
        print("👉 Starting ingest...")

        text = load_pdf("hospital.pdf")
        print("👉 PDF loaded")

        chunks = chunk_text(text)
        print("👉 Total chunks:", len(chunks))

        # ❗ CHECK
        if len(chunks) == 0:
            return {"error": "No text found in PDF"}

        embeddings = get_embeddings(chunks)
        print("👉 Embeddings done")

        store_chunks(chunks, embeddings)
        print("👉 Stored in DB")

        return {"message": "✅ Data stored successfully!"}

    except Exception as e:
        print("❌ ERROR:", e)
        return {"error": str(e)}

@app.post("/query")
def query(q: Query):
    query_embedding = model.encode([q.question])[0]

    results = search_similar(query_embedding)

    print("👉 Results:", results)   # 🔥 ADD THIS

    if not results:
        return {"answer": "No data found"}

    context = " ".join([r["content"] for r in results])

    print("👉 Context:", context[:500])  # 🔥 ADD THIS

    answer = generate_answer(context, q.question)

    return {
        "answer": answer,
        "sources": ["top matches"]
    }