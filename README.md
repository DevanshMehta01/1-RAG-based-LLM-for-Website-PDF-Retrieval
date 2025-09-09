RAG-LLM: Retrieval from Websites & PDFs
What is this project about?

This project demonstrates how to build a Retrieval-Augmented Generation (RAG) application.

You can either:

Provide a website URL, and the app scrapes and indexes its content

Upload a PDF, and the app parses and indexes the document

Once indexed, you can ask natural language questions, and the system uses a vector database + LLM to retrieve and generate accurate answers.

The goal is to show how LLMs can be made practically useful for tasks like knowledge management, document search, and customer support.

Key Features

Scrape website content and make it searchable

Upload PDFs and extract text for Q&A

Semantic search with FAISS (not just keyword matching)

Question answering powered by Groq (Qwen3-32B model)

Simple Streamlit UI for interaction

Ready for deployment with Docker or Hugging Face Spaces

Tech Stack

LangChain – RAG pipeline orchestration

HuggingFace Embeddings + FAISS – semantic search

Groq API (Qwen3-32B) – LLM inference

BeautifulSoup + PyPDF2 – content extraction

Streamlit – interactive frontend
