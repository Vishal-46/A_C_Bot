from botcore.loader import load_and_split_documents
chunks = load_and_split_documents("data/sd.pdf")
print(f"Loaded {len(chunks)} chunks.")
if chunks:
    print(chunks[0].page_content[:300])
else:
    print("No content was loaded. Check file path or document parsing.")
