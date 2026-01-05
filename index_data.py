from langchain_community.document_loaders import WebBaseLoader
loader= WebBaseLoader(web_paths=["https://bikanervala.com/collections/sweets"])
docs=loader.load()

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=50)
splits = text_splitter.split_documents(docs)


from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore= Chroma.from_documents(documents=splits, embedding=embeddings, persist_directory="./chroma_db")
vectorstore.persist()
print("✅ Chroma DB created and persisted successfully.")