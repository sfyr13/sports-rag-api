# from fastapi import FastAPI

# app = FastAPI(title="Sports Wiki RAG API")

# @app.get("/")
# def root():
#     return {"message": "Sports RAG API is running"}

from services.wiki_service import search_wikipedia, get_page_content
from services.chunker import chunk_text


results = search_wikipedia("Lionel Messi")

print(results)

page = None

for r in results:
    p = get_page_content(r)
    if p["content"] and len(p["content"]) > 100:  # Only consider pages with content longer than 100 characters
        page = p
        break


print("Title:", page["title"])
print("Content length:", len(page["content"]))

chunks = chunk_text(page["content"])

print(f"Number of chunks: {len(chunks)}")

if chunks:
    print(chunks[0][:500])