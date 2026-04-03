from supabase import create_client

SUPABASE_URL = "https://odjdpiwqkraifoyrnoyn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9kamRwaXdxa3JhaWZveXJub3luIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzUxOTY5NjQsImV4cCI6MjA5MDc3Mjk2NH0.sct8CvaHizMQVf0wxcJ24EXTCyrhi8Yun-dx1pUlj8I"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def store_chunks(chunks, embeddings):
    for i in range(len(chunks)):
        supabase.table("documents").insert({
            "content": chunks[i],
            "embedding": embeddings[i].tolist()
        }).execute()

def search_similar(query_embedding):
    response = supabase.rpc("match_documents", {
        "query_embedding": query_embedding.tolist(),
        "match_count": 3
    }).execute()

    return response.data



