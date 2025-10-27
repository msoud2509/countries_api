from data_loader import load_data
from contextlib import asynccontextmanager
from countries_api import router
from fastapi import FastAPI

import logging
logging.basicConfig(level=logging.INFO)

import sys
import uvicorn
LOCAL_IP = "127.0.0.1"
HOSTED_IP = "0.0.0.0"

LOCAL_PORT = 8080
HOSTED_PORT = 8080

GRAPH_DATA = None
SRC_COUNTRY = "USA"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # load data into memory on startup
    global GRAPH_DATA
    try:
        GRAPH_DATA = load_data('countries_graph.json')
    except Exception as e:
        logging.error(f"Error loading graph data: {e}")
    if not GRAPH_DATA:
        raise ValueError("Failed to load graph data on startup")

    yield # server running

app = FastAPI(
    title="Country Path Finder API",
    description="API to find shortest path between countries using BFS",
    version="1.0.0",
    lifespan=lifespan
)
app.include_router(router)

if __name__ == "__main__":
    is_local = True if "--local" in sys.argv else False
    if is_local:
        uvicorn.run("main:app", host=LOCAL_IP, port=LOCAL_PORT, reload=True)
    else:
        uvicorn.run("main:app", host=HOSTED_IP, port=HOSTED_PORT)
