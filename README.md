# A_C_Bot
## File Structure 
```
rag_chatbot/
├── app.py                          # Main Streamlit application
├── config/
│   └── settings.py                 # Configuration settings
├── src/
│   ├── __init__.py
│   ├── document_processor.py       # Document loading and preprocessing
│   ├── vector_store.py            # FAISS vector database operations
│   ├── embeddings.py              # Embedding model management
│   ├── retriever.py               # Document retrieval logic
│   └── generator.py               # Response generation
├── data/
│   ├── documents/                 # Raw documents (PDF, TXT, etc.)
│   └── processed/                 # Processed chunks and metadata
├── models/
│   └── faiss_index/              # FAISS index files
├── requirements.txt               # Python dependencies
├── utils/
│   ├── __init__.py
│   └── helpers.py                # Utility functions
└── README.md
```