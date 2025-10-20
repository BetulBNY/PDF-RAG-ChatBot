# We will process our LLM chain here

import os
from dotenv import load_dotenv
#from langchain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA # FAISS, Chroma, Pinecone gibi bir vektör veritabanlarından kullanıcı sorusuyla en alakalı belgelerigetirir.
from langchain_google_genai import ChatGoogleGenerativeAI 


load_dotenv() # for upload .env variables 

# Reading API KEY
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_llm_chain(vectorstore):  # GİRDİ: retriever: Vektör veritabanından ilgili bilgi parçalarını getiren sistem.
    llm = ChatGoogleGenerativeAI(
            model = "gemini-2.5-flash-lite", 
            temperature=0.3 # Cevapların daha tutarlı olması için sıcaklığı biraz düşürebiliriz
    )
    retriever=vectorstore.as_retriever(search_kwargs={"k":3})
    # Daha kontrollü ve özelleştirilebilir istiyorsan buraya Prompt ekleyebilirsin

    return RetrievalQA.from_chain_type(
        llm = llm,
        chain_type = "stuff",
        retriever = retriever,
        return_source_documents = True
    )



                
"""
[User Question]
       ↓
   Retriever (Chroma)
       ↓
     Context
       ↓
   LLM (Gemini)
       ↓
     Answer
"""



"""
ÖRNEK AKIŞ
Kullanıcı: “Bu ilaç hangi hastalık için kullanılır?”
retriever → PDF içinde ilgili sayfaları bulur (örneğin “ibuprofen” sayfası).
prompt → “Context” kısmına bu sayfa eklenir, “Question” kısmına kullanıcı sorusu.
Gemini → bu bilgiden cevabı üretir.
RetrievalQA → cevabı döndürür.
| Bölüm                    | Ne işe yarar             | Açıklama                             |
| ------------------------ | ------------------------ | ------------------------------------ |
| `PromptTemplate`         | Prompt şablonu oluşturur | Context + Question yapısı            |
| `RetrievalQA`            | RAG zinciri oluşturur    | Retriever + LLM’i birleştirir        |
| `ChatGoogleGenerativeAI` | Gemini LLM wrapper’ı     | Google API’sini LangChain ile bağlar |
| `dotenv`                 | API key yükler           | `.env` dosyasını okur                |
| `temperature`            | Cevap tutarlılığı        | Düşükse daha kesin cevap verir       |
"""
