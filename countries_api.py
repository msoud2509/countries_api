from fastapi import APIRouter, Depends, HTTPException
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
    try:
        result = bfs(graph, SRC_COUNTRY, country)
    except Exception:
        raise HTTPException(status_code=500, detail=f"Error executing BFS")
    if result:
        return {"status_code": 200, "data": result}
    else:
        return {"status_code": 404, "detail": f"Path to country '{country}' not found"}
