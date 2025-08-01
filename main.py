from typing import AsyncGenerator

from fastapi import Depends, FastAPI
from streaq import Worker

from example import fetch, worker

app = FastAPI()

async def get_worker() -> AsyncGenerator[Worker, None]:
    async with worker:
        yield worker

@app.get("/enqueue", dependencies=[Depends(get_worker)])
async def enqueue(url: str) -> bool:
    task = await fetch.enqueue(url)
    res = await task.result(5)
    return res.success