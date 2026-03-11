import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

def create_vector_store(chunks):
    """
    Convert text chunks into embeddings and store them in ChromaDB.
    """
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma.from_texts(
        texts=chunks,
        embedding=embeddings,
        collection_name="sports_wiki"
    )

    return vector_store