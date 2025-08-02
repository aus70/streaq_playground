from fastapi import FastAPI

from example import fetch

app = FastAPI()

@app.get("/enqueue")
async def enqueue(url: str) -> bool:
    task = await fetch.enqueue(url)
    res = await task.result(5)
    return res.success