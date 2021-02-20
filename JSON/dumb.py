import json

python_dict = {"name": "Aum", "age": 20, "city": "Bangkok"}

json_string = json.dumps(python_dict)

print(json_string)