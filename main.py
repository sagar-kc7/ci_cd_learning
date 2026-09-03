from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Concurrency test B"}

@app.get("/health")
def health():
    return {"status": "healthy"}