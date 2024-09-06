from src.helper import load_pdf, textSplitter, download_embeddings
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

data = load_pdf()
text_chunks = textSplitter(data)
embeddings = download_embeddings()

# Creating vectors to insert in PineCone Database

import uuid
data = []
for i in range(0 , len(text_chunks)):
    dic = {}
    dic["id"] = str(uuid.uuid4())
    dic["values"] = embeddings.embed_query(text_chunks[i].page_content)
    dic["metadata"] = {"data" : text_chunks[i].page_content}
    data.append(dic)


# Configuring PineCone Connection
import google.api
from pinecone.grpc import PineconeGRPC as Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
indexName = "medchatbot"
index = pc.Index(indexName)

# Upserting data to PineCone Database
index.upsert(vectors = data)