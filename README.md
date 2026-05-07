# RAG Project

A production-ready Retrieval-Augmented Generation (RAG) application built using Python, LangChain, ChromaDB, Streamlit, and Mistral AI models.  
This project enables users to upload PDF/text documents and ask contextual questions with AI-powered responses.

---

# 🚀 Features

- 📄 PDF & Text Document Processing
- 🔍 Semantic Search using Vector Embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- 🤖 Conversational AI with Mistral LLMs
- ⚡ Fast Document Retrieval with ChromaDB
- 💬 Context-Aware Question Answering
- 🌐 Streamlit Interactive UI
- 🧩 Modular Project Structure
- 📚 Multi-Document Support

---

# 🛠️ Tech Stack

## Core Technologies
- Python
- LangChain
- Streamlit
- ChromaDB
- Mistral AI
- Hugging Face

## AI & NLP
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Embeddings
- Prompt Engineering
- Text Chunking
- Vector Databases

---

# 📂 Project Structure

```bash
RAG Project/
│
├── document loaders/
│   ├── GRU.pdf
│   ├── deeplearning.pdf
│   ├── notes.txt
│   ├── page.py
│   └── pdf.py
│
├── vector store/
│   └── db.py
│
├── app.py
├── create database.py
├── test.py
├── requirements.txt
```

---

# 📌 Project Workflow

## 1️⃣ Document Loading
Loads PDF and text documents using LangChain document loaders.

## 2️⃣ Text Splitting
Splits documents into smaller chunks for efficient retrieval.

## 3️⃣ Embedding Generation
Creates vector embeddings using Mistral Embeddings.

## 4️⃣ Vector Storage
Stores embeddings inside ChromaDB for semantic search.

## 5️⃣ Retrieval
Retrieves relevant chunks based on user query.

## 6️⃣ AI Response Generation
Uses Mistral LLM to generate accurate contextual answers.

---

# ⚙️ Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd RAG-Project
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key_here
```

Get API Key from:
https://console.mistral.ai

---

# ▶️ Run Project

## Create Vector Database

```bash
python create_database.py
```

## Start Streamlit App

```bash
streamlit run app.py
```

---

# 🧠 Example Use Cases

- AI PDF Assistant
- Research Paper Q&A
- Notes Summarization
- AI Study Assistant
- Document Search Engine
- Enterprise Knowledge Base

---

# 📈 Future Improvements

- Multi-PDF Upload
- Chat Memory
- Hybrid Search
- Agentic RAG
- Voice Assistant
- Web Deployment
- Authentication System

---

# 👨‍💻 Author

## Sanjeev Gupta

- GitHub: https://github.com/Sanjeevgupta2000
- LinkedIn: https://linkedin.com/in/Sanjeev-gupta-a7611a1b9

---

# ⭐ Key Highlights

- Built using modern Generative AI architecture
- Uses Retrieval-Augmented Generation (RAG)
- Production-ready modular structure
- Optimized semantic retrieval pipeline
- Real-world AI application project

---

# 📜 License

This project is open-source and available for educational and learning purposes.
