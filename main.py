from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Added staging and production environments"}

@app.get("/health")
def health():
    return {"status": "healthy"}