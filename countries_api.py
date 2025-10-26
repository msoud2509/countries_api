from fastapi import APIRouter, Depends
from bfs_script import bfs

router = APIRouter()

def get_countries_graph():
    from main import GRAPH_DATA
    if GRAPH_DATA is None:
        raise ValueError("Graph data is not loaded")
    return GRAPH_DATA

@router.get("/{country}")
def bfs_route(country: str, graph: dict = Depends(get_countries_graph)):
    """
    Find shortest path from USA to input country.

    Args:
        country: Destination country code
        graph: Countries adjacency graph, loaded on startup from main.py
    """
    country = country.upper() # make case-insensitive

    from main import SRC_COUNTRY
    result = bfs(graph, SRC_COUNTRY, country)
    return {"path": result}
