from fastapi import FastAPI

app = FastAPI(title="ml-prod-48d")

@app.get("/health")
def health():
    return {"status": "ok"}
