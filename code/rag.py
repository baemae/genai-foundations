from langchain.chat_models import init_chat_model
from langchain_community.document_loaders import TextLoader #LLM
from Langchain.embeddings import init_embedding_model #embedding model
from langchain_core.vectorstores import InMemoryVectorStore, Inmemoryvectorstore #vectorstore
from langchain_community.document_loaders import TextLoader, PyPDFLoader #document loader
from langchain_text_splitters import RecursiveCharacterTextSplitter #text splitter fpr chunks
#need to install langchain_community, langchain_text_splitters, langchain_core for complete RAG

chunks = RecursiveCharacterTextSplitter( chunks=500, chunk_overlap=75)
vs = InMemoryVectorStore(embedding=init_embedding_model(model="nomic-embed-text:latest", model_provider="ollama"))
llm = init_chat_model(
    model="gemma3:1b", provider="ollama"
)



cxt = ""

#step 1: Retrieval

#step 2: Generation


