from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Testing safe deployment"}

@app.get("/health")
def health():
    return {"status": "healthy"}