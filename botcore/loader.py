from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
def load_and_split_documents(filepath):
    loader = PyPDFLoader(filepath)
    docs = loader.load()
    print(f"Loaded {len(docs)} document pages.")
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    print(f"Split into {len(chunks)} chunks.")
    return chunks
