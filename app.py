
import os
import streamlit as st
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from tempfile import NamedTemporaryFile
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings



load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(page_title="RAG-LLM", page_icon="", layout="wide")
st.title("RAG-based LLM for Website & PDF Retrieval")

def scrape_text_from_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator="\\n")

def extract_text_from_pdf(uploaded_file) -> str:
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\\n"
    return text

def create_vectorstore_from_text(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    docs = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_texts(docs, embeddings)
    return vectorstore

def run_qa_chain(vectorstore, query):
    retriever = vectorstore.as_retriever()
    llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name="qwen/qwen3-32b")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(query)
def clean_response(response):
    if "think>" in response:
        return response.split("think>")[-1].strip().split("\n", 1)[-1]
    return response.strip()


st.sidebar.header("Input Options")
input_mode = st.sidebar.radio("Select Input Type:", ["URL", "Upload PDF"])

vectorstore = None

if input_mode == "URL":
    url = st.sidebar.text_input("Enter Website URL")
    if st.sidebar.button("Scrape & Index URL"):
        if url:
            with st.spinner("Scraping and indexing URL content..."):
                try:
                    raw_text = scrape_text_from_url(url)
                    vectorstore = create_vectorstore_from_text(raw_text)
                    st.success("Website content indexed successfully!")
                    st.session_state['vectorstore'] = vectorstore
                except Exception as e:
                    st.error(f"Failed to scrape URL: {e}")
        else:
            st.sidebar.warning("Please enter a valid URL.")

elif input_mode == "Upload PDF":
    pdf_file = st.sidebar.file_uploader("Upload PDF file", type=["pdf"])
    if pdf_file and st.sidebar.button("Index PDF"):
        with st.spinner("Extracting and indexing PDF..."):
            try:
                raw_text = extract_text_from_pdf(pdf_file)
                vectorstore = create_vectorstore_from_text(raw_text)
                st.success("PDF content indexed successfully!")
                st.session_state['vectorstore'] = vectorstore
            except Exception as e:
                st.error(f"Failed to process PDF: {e}")


if 'vectorstore' in st.session_state and st.session_state['vectorstore']:
    query = st.text_input("Ask a question about the indexed content:")
    if query:
        with st.spinner("Generating answer..."):
            try:
                answer = run_qa_chain(st.session_state['vectorstore'], query)
                st.markdown("###  Answer:")
                
                st.write(clean_response(answer))   
            except Exception as e:
                st.error(f"Failed to generate answer: {e}")
else:
    st.info("Provide some content via URL or PDF upload to start asking questions.")
