import json
from urllib.parse import parse_qs

with open("q-vercel-python.json") as f:
    data = json.load(f)

marks_dict = {entry["name"]: entry["marks"] for entry in data}

def handler(request, response):
    # Parse query parameters
    qs = parse_qs(request.query_string.decode())
    names = qs.get("name", [])
    # Look up marks for each name, default to None if not found
    marks = [marks_dict.get(n, None) for n in names]
    # Set CORS headers
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"] = "application/json"
    # Respond with JSON
    response.body = json.dumps({"marks": marks}).encode()
    return response
