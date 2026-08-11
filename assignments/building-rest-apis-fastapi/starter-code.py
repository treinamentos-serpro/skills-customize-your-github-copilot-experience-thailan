from fastapi import FastAPI

app = FastAPI(title="Simple API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
