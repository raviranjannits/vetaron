from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

def load_pdf():
    loader = PyPDFLoader("C:/Users/Mrinal/Desktop/MedicalChatbot/data/AnimalDisease.pdf")
    pages = loader.load_and_split()
    return pages

def textSplitter(pages):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 200 , chunk_overlap = 20)
    text_chunks = text_splitter.split_documents(pages)
    return text_chunks

def download_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings
