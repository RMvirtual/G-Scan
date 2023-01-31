import json


def load_json(path: str) -> dict[str, any]:
    with open(path, "r") as file_stream:
        return json.loads(file_stream.read())
