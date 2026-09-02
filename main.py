from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Version 2 deployed successfully!"}

@app.get("/health")
def health():
    return {"status": "ok"}