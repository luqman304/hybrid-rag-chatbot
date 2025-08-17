Hybrid RAG Chatbot 🤖📚  

A conversational assistant that combines **retrieval-based search (RAG)** with **generative AI** to answer queries from a custom knowledge base. The system retrieves relevant passages from documents and generates responses grounded in that content.  

---

## 🚀 Features
- 📂 **Document ingestion** — load Markdown, text, or PDFs  
- 🔎 **Retrieval layer** — TF-IDF search (with upgrade path to embeddings + FAISS/Pinecone)  
- 🧠 **Generative layer** — contextual, natural responses (can plug in Hugging Face or OpenAI models)  
- 💬 **Web interface** — Streamlit app for interactive Q&A  
- 🔌 **Extensible** — easy to integrate more data sources or models  

---

## 🛠️ Tech Stack
- **Python 3.9+**  
- **Streamlit** — frontend Q&A app  
- **Scikit-learn** — TF-IDF vectorizer  
- **FAISS or Pinecone (optional)** — scalable vector search  
- **Hugging Face Transformers / OpenAI (optional)** — LLM integration  

---

## 📦 Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/luqman304/hybrid-rag-chatbot.git
cd hybrid-rag-chatbot
pip install -r requirements.txt
```

---

## ▶️ Usage
1. Place your knowledge base files in the `data/` folder (Markdown, `.txt`, `.pdf`).  
2. Run the chatbot:  
   ```bash
   streamlit run app.py
   ```  
3. Ask a question in the web interface and get an answer grounded in your documents.  

---

## 📁 Project Structure
```
hybrid-rag-chatbot/
│── app.py               # Streamlit chatbot app
│── retriever.py         # TF-IDF (or embeddings) retrieval
│── generator.py         # Generative response layer
│── requirements.txt     # Dependencies
│── data/                # Knowledge base docs
│── README.md            # Project description
```

---

## 🔮 Upgrade Ideas
- Replace TF-IDF with **embeddings (SentenceTransformers)**  
- Swap generative layer for **LLM API (OpenAI GPT, Hugging Face models)**  
- Integrate **Neo4j** for knowledge graph retrieval  
- Add **conversation history memory**  

---

## 📌 Example Use Cases
- **Enterprise knowledge assistant** (query company documents)  
- **Customer support bot** (answer FAQs with real context)  
- **Academic helper** (summarize and answer from papers/notes)  

---

## 📜 License
© 2025 Luqman Abdulwahab.  
This project is proprietary. No part may be used, modified, or distributed without explicit permission.  
