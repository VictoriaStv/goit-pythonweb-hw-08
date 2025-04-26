from fastapi import FastAPI
from src.routes import router

app = FastAPI(title="Contacts API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "🚀 Contacts API is running!"}
