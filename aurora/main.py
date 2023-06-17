import logging
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from langchain.embeddings import LlamaCppEmbeddings
from langchain.vectorstores import VectorStore, Qdrant
import qdrant_client

app = FastAPI()
templates = Jinja2Templates(directory="web")

embeddings = None
vectorstore: Optional[VectorStore] = None

@app.on_event("startup")
async def startup_event():
    global embeddings
    global vectorstore

    logging.info("loading embeddings")
    embeddings = LlamaCppEmbeddings(model_path="./model.bin")

    logging.info("loading vectorstore")
    client = qdrant_client.QdrantClient(path="./qdrant.db", prefer_grpc=True)
    vectortore = Qdrant(client=client, collection_name="my_documents", embeddings=embeddings)

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)

