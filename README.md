RAG-LLM: Smart Retrieval from Websites & PDFs

 What’s this about?
 
Finding information inside long PDFs or across websites can be time-consuming.
This project tackles that problem by building a Retrieval-Augmented Generation (RAG) system that:
-Takes a website link or an uploaded PDF
-Extracts and indexes the content as embeddings
-Stores knowledge as embeddings and lets a Large Language Model answer your questions conversationally.  
This isn’t just a toy — it’s a real-world style app people can imagine being used in knowledge management, document search, or customer support.

Highlights:
Purpose:
The project builds a Retrieval-Augmented Generation (RAG) system that lets users query web or PDF content and get accurate, context-aware answers.

Motivation:
Designed to make LLMs more factually grounded by allowing them to access real-time or external information instead of relying only on pretrained data.

User Interaction:
Users provide either a website URL or PDF file, and the system extracts and processes text automatically through a Streamlit interface.

Data Extraction:
BeautifulSoup handles web scraping, while PyPDF2 processes PDF documents, converting everything into clean text.

Text Chunking:
The text is split into small, overlapping pieces using RecursiveCharacterTextSplitter, preserving context across chunks.

Embeddings:
Each text chunk is converted into a dense vector embedding using HuggingFaceEmbeddings, capturing its semantic meaning.

Vector Storage:
These embeddings are stored and indexed in FAISS (Facebook AI Similarity Search) — an in-memory vector database for fast similarity search.

Query Processing:
When the user submits a query, it’s also converted into an embedding, and FAISS retrieves the most relevant text chunks from the database.

Answer Generation:
The retrieved chunks are combined with the user’s query via LangChain’s RetrievalQA (stuff chain) and passed to the Groq Qwen-3 32B LLM, which generates the final answer.

Security & Deployment:
API keys (like GROQ_API_KEY) are stored securely in a .env file and loaded using python-dotenv. The system runs efficiently and locally with minimal setup.

 Tech in Action
1. LangChain for RAG pipeline
2. HuggingFace embeddings + FAISS for vector search
3. Groq API (LLM) for fast, smart answers
4. BeautifulSoup + PyPDF2 for scraping & parsing
5. Streamlit for the interactive UI


   

