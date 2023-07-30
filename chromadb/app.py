import chromadb
import chromadb.config
from chromadb.server.fastapi import FastAPI

settings = chromadb.config.Settings()
# enable SSL for Railway
settings.chroma_server_ssl_enabled = True
server = FastAPI(settings)
app = server.app()
