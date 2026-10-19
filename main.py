from fastapi import FastAPI
from app.routers import tasks

app = FastAPI()

app.include_router(tasks.router)

@app.get("/health")
def healt_check():
    return {"message": "The API is running properly"}