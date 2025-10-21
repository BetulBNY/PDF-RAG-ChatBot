# 📚 PDF-RAG-ChatBot

An intelligent chatbot that allows users to upload PDFs and ask questions based on their content.  
Built with Retrieval-Augmented Generation (RAG) for accurate, context-aware answers.  
Powered by FastAPI, Streamlit, and Google’s API.

---

## 🧠 Features

✅ Upload one or more PDF files  
✅ Ask natural language questions about the document  
✅ Uses RAG pipeline (Retriever + LLM + Memory)  
✅ Fast, interactive interface built with Streamlit  
✅ Backend powered by FastAPI  
✅ Supports persistent vector storage (ChromaDB)  

---

## 🏗️ Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | Streamlit |
| **Backend** | FastAPI |
| **LLM Integration** | Google API |
| **Vector Database** | Chroma |
| **Document Parsing** | PyPDF2 / LangChain Document Loaders |

---

## ⚙️ Installation
```bash

1️⃣ Clone the repository
git clone https://github.com/BetulBNY/PDF-RAG-ChatBot.git
cd PDF-RAG-ChatBot


2️⃣ Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set your API key
Create a .env file in the project root and add:
GOOGLE_API_KEY=your_api_key_here

▶️ Run the Project

Run the FastAPI backend
uvicorn backend.main:app --reload

Run the Streamlit frontend
streamlit run app.py


💬 Example Usage
Upload a PDF (e.g., “AI Whitepaper.pdf”)

Ask:
“Summarize the main idea of section 3.”
“What are the key advantages of this model?”

The chatbot retrieves the most relevant chunks and generates a contextual answer.
