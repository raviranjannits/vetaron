from src.helper import download_embeddings
from dotenv import load_dotenv
import os

load_dotenv()
embeddings = download_embeddings()

#Getting Keys from .env file
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")


# Create a Pinecone index
from pinecone.grpc import PineconeGRPC as Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
indexName = "medchatbot"
index = pc.Index(indexName)

# Logging into HuggingFace hub
from huggingface_hub import login

# Authenticate with Hugging Face using your token
login(token=HUGGINGFACE_API_KEY)
from langchain_huggingface import HuggingFaceEndpoint
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=128,
    temperature=0.5,
    huggingfacehub_api_token=HUGGINGFACE_API_KEY,
)
def generateAnswer(ques):
    query = ques
    print (index.describe_index_stats())
    docs = index.query(
        #namespace="example-namespace",
        vector = embeddings.embed_query(query),
        top_k=3,
        include_values=True ,
        include_metadata=True
    )

    Data=""
    for data in docs["matches"]:
        Data += data["metadata"]["data"]
        Data+="\n"

    prompt = f"""
    Use the following pieces of information to answer the user's question.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    Context: {Data}
    Question: {ques}

    Only return the helpful answer below and nothing else.
    Helpful answer:
    """
    response = llm(prompt)

    return response

ques = input("Ask your question")
print(generateAnswer(ques))