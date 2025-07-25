import streamlit as st
from botcore.vector_db import create_and_save_index, load_subject_index, search_index
st.title(" Academic Assistant Bot")
db = load_subject_index()
query = st.text_input("Ask a question based on your syllabus...")
if query:
    results = search_index(query, db)
    for i, res in enumerate(results):
        st.markdown(f"**Result {i+1}:** {res.page_content}")
