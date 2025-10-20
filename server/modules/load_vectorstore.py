import os
from pathlib import Path
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# We will store our embedede vectors of PDFs into directory called Chroma

PERSIST_DIR="./chroma_store" # ChromaDB’nin vektörleri kalıcı olarak kaydedeceği klasör
UPLOAD_DIR="./uploaded_pdfs" # Kullanıcının yüklediği PDF dosyalarının geçici olarak saklanacağı klasör
os.makedirs(UPLOAD_DIR,exist_ok=True) # Klasör yoksa oluşturur, varsa hata vermez

def load_vectorstore(uploaded_files):
    file_paths=[]

    # Save PDF files
    for file in uploaded_files:
        save_path=Path(UPLOAD_DIR)/file.filename
        with open(save_path,"wb") as f:
            f.write(file.file.read())
        file_paths.append(str(save_path))

    # Load PDF files
    docs = []  # In the docs list, each page is available as a LangChain Document object
    for path in file_paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())

    # Separating chunks
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(docs)
 
    # Embedding these chunks
    embeddings = HuggingFaceBgeEmbeddings(model_name = "all-MiniLM-L12-v2")

    if os.path.exists(PERSIST_DIR) and  os.listdir(PERSIST_DIR):
        vectorstore=Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
        vectorstore.add_documents(texts)
        vectorstore.persist()
    else:
        vectorstore=Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory=PERSIST_DIR
        )
        vectorstore.persist()

    return vectorstore    