import json

def process_json(data: dict, filename: str):
    
    # Serialize the dictionary to a JSON file
    json_string = json.dumps(data, indent=4)
    with open(filename, 'w') as json_file:
        json_file.write(json_string)

process_json({'name': 'Alice', 'age': 30, 'city': 'New York'}, 'output.json')