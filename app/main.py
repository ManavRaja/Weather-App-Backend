from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """Root route that doesn't have any use."""
    return {"message": "Hello World"}
