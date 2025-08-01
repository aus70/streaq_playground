from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import AsyncIterator
from streaq import Worker

@dataclass
class WorkerContext:
    ...

@asynccontextmanager
async def lifespan() -> AsyncIterator[WorkerContext]:
    print("Starting worker lifespan")
    yield WorkerContext()
    print("Ending worker lifespan")

worker = Worker(redis_url="redis://localhost:6379", lifespan=lifespan)

@worker.task(timeout=5)
async def fetch(url: str) -> int:
    print(f"Fetching URL: {url}")
    return 42
