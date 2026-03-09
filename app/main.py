# from fastapi import FastAPI

# app = FastAPI(title="Sports Wiki RAG API")

# @app.get("/")
# def root():
#     return {"message": "Sports RAG API is running"}

from services.wiki_service import search_wikipedia, get_page_content


results = search_wikipedia("Lionel Messi")

print(results)

page = get_page_content(results[0])

print(page["title"])
print(page["content"][:500])