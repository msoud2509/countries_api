import json

def load_data(file_path: str) -> dict:
    """
    Load data from a JSON file and return as a dictionary.

    Args:
        file_path: Path to the JSON file.
    Returns:
        Dictionary representing the data, or None if loading fails.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        return None