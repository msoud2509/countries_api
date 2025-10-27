from collections import deque

import logging
logging.basicConfig(level=logging.INFO)

def bfs(graph: dict, src_country: str, dst_country: str) -> list:
    """
    Find the shortest path (min number of country border crossings) from src_country to dst_country using BFS.
    
    Args:
        graph: Dictionary representing adjacency list
        src_country: Starting country code
        dst_country: Destination country code
    
    Returns:
        List of country codes representing the shortest path,
        or None if no path exists
    """
    if src_country not in graph:
        logging.warning(f"Source country {src_country} not in graph.")
        return None
    
    if src_country == dst_country:
        return [src_country]
    
    try:
        visited = set([src_country])
        queue = deque([(src_country, [src_country])])  # queue of (current_node, path_to_current_node)

        while queue:
            cur_country, path = queue.popleft()
            
            for neighbor in graph.get(cur_country, []):
                if neighbor == dst_country:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
    except Exception as e:
        raise Exception(f"Error executing BFS: {e}")
    
    # no path found
    logging.warning(f"No path found from {src_country} to {dst_country}.")
    return None