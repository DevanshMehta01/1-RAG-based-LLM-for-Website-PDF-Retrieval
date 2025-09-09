RAG-LLM: Smart Retrieval from Websites & PDFs

 What’s this about?
 
Finding information inside long PDFs or across websites can be time-consuming.
This project tackles that problem by building a Retrieval-Augmented Generation (RAG) system that:
-Takes a website link or an uploaded PDF
-Extracts and indexes the content as embeddings
-Stores knowledge as embeddings and lets a Large Language Model answer your questions conversationally.  
This isn’t just a toy — it’s a real-world style app people can imagine being used in knowledge management, document search, or customer support.

 Highlights
 
 1. Scrape any website → instantly index the content
 2. Upload PDFs → parse text and make it searchable
 3. Semantic search with FAISS → finds meaning, not just keywords
 4. Groq-powered Qwen3-32B LLM → answers feel natural, not robotic
 5. Streamlit UI → simple, clean, recruiter-friendly demo
 6. Deployable with Docker / Hugging Face Spaces

 Tech in Action
 
1. LangChain for RAG pipeline
2. HuggingFace embeddings + FAISS for vector search
3. Groq API (Qwen3-32B) for fast, smart answers
4. BeautifulSoup + PyPDF2 for scraping & parsing
5. Streamlit for the interactive UI

