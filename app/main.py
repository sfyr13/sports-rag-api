from fastapi import FastAPI

app = FastAPI(title="Sports Wiki RAG API")

@app.get("/")
def root():
    return {"message": "Sports RAG API is running"}