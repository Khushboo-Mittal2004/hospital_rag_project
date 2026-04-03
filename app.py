import streamlit as st
import requests

st.title("🏥 AI Hospital Assistant")

question = st.text_input("Ask your question")

if st.button("Ask"):
    res = requests.post(
        "http://127.0.0.1:8000/query",
        json={"question": question}
    )

    st.write(res.json()["answer"])