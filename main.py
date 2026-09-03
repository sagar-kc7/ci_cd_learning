from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Concurrency test A"}

@app.get("/health")
def health():
    return {"status": "healthy"}