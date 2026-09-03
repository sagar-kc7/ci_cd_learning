from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Updated Trust Policy #4"}

@app.get("/health")
def health():
    return {"status": "healthy"}