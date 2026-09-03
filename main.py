from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Healthy deployment"}

@app.get("/health")
def health():
    return {"status": "ok"}