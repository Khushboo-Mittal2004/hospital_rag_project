from groq import Groq

client = Groq(api_key="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")

def generate_answer(context, question):

    prompt = f"""
You are a hospital assistant.

Answer ONLY using the context below.
If a number is present, ALWAYS include it in the answer.

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
  
  