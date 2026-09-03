from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Testing safe deployment"}

@app.get("/health")
def health():
    raise HTTPException(status_code=500, detail="Intentional failure")