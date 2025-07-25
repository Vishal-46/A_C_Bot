import os
from botcore.loader import load_and_split_documents
from botcore.vector_db import embed_chunks, store_subject_index

data_folder = "data"

for filename in os.listdir(data_folder):
    if filename.endswith(".pdf"):
        subject_code = filename.replace(".pdf", "")
        print(f"Processing {subject_code}...")
        chunks = load_and_split_documents(os.path.join(data_folder, filename))
        embeddings = embed_chunks(chunks)
        store_subject_index(subject_code, embeddings, chunks)

print("All subject indexes built!")
