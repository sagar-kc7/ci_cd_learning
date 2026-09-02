from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "CI/CD deployment works1"}

@app.get("/health")
def health():
    return {"status": "ok"}