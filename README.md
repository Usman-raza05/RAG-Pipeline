
# Python RAG Pipeline

A Retrieval-Augmented Generation (RAG) application built with Python that allows users to ask questions about their documents and receive AI-generated answers based on relevant retrieved context.

The project combines semantic search, vector embeddings, FAISS vector storage, and Groq LLMs to build a document-based question-answering system.

## Overview

Traditional LLMs generate answers using their pre-trained knowledge. RAG improves this process by retrieving relevant information from external documents before generating a response.

This project follows a simple RAG workflow:

1. Load documents from PDF files.
2. Split documents into smaller chunks.
3. Generate vector embeddings using Sentence Transformers.
4. Store embeddings in a FAISS vector database.
5. Retrieve relevant chunks based on a user's query.
6. Pass the retrieved context to a Groq LLM.
7. Generate a context-based response.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Document loading and text splitting |
| Sentence Transformers | Text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| FAISS | Vector similarity search |
| Groq | LLM inference |
| Jupyter Notebook | Experimentation and learning |
| python-dotenv | Environment variable management |

## Project Structure

```text
RAG/
│
├── data/
│   ├── pdf/                 # PDF documents (local)
│   └── text_files/          # Sample text documents
│
├── faiss_store/             # Generated FAISS index (local)
│
├── notebook/
│   ├── document.ipynb
│   └── pdf_loader.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py       # Document loading
│   ├── embedding.py         # Chunking and embeddings
│   ├── vectorstore.py       # FAISS vector database
│   └── search.py            # Retrieval and LLM response
│
├── .env                     # API keys (not committed)
├── .gitignore
├── app.py                   # Application entry point
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Usman-raza05/RAG-Pipeline.git
cd RAG
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

Using pip:

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

**Important:** Never commit your `.env` file or expose your API key publicly.

### 5. Add Your Documents

Place your PDF documents inside:

```text
data/pdf/
```

The document loader currently supports PDF ingestion.

### 6. Run the Application

```bash
python app.py
```

The application will load or build the FAISS vector store, retrieve relevant document chunks, and generate an answer using the configured Groq model.

## RAG Architecture

```text
        PDF Documents
              |
              v
       Document Loader
              |
              v
       Text Splitter
              |
              v
      Sentence Transformers
              |
              v
        Text Embeddings
              |
              v
         FAISS Store
              |
              |
        User Question
              |
              v
       Query Embedding
              |
              v
       Similarity Search
              |
              v
      Relevant Documents
              |
              v
          Groq LLM
              |
              v
       Generated Answer
```

## Models

**Embedding Model**

`sentence-transformers/all-MiniLM-L6-v2`

Used to convert document chunks and user queries into numerical vector representations.

**Language Model**

`openai/gpt-oss-20b`

Used through Groq for generating responses from retrieved document context.

## Current Features

- PDF document loading
- Document text chunking
- Semantic vector embeddings
- FAISS-based vector search
- Persistent vector storage
- Groq LLM integration
- Context-based question answering
- Jupyter Notebook experiments

## Future Improvements

- Support for DOCX, TXT, CSV, and Excel documents
- Improved retrieval and reranking
- Better source attribution and citations
- Conversational memory
- Streamlit or FastAPI interface
- More advanced RAG evaluation
- Improved handling of conflicting or missing information

## Learning Objectives

This project is also a hands-on learning journey covering:

- Understanding Retrieval-Augmented Generation
- Working with embeddings and vector databases
- Building document processing pipelines
- Implementing semantic search
- Integrating LLM APIs
- Structuring Python applications into reusable modules

## Author

**Usman Raza**

GitHub: [Usman-Raza05](https://github.com/Usman-Raza05)

---

*Built as a practical project to understand and implement Retrieval-Augmented Generation using Python.*
