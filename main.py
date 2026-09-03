from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Version 3 - broken deployment"}

@app.get("/health")
def health():
    raise HTTPException(status_code=500, detail="Intentional failure")