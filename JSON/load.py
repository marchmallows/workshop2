import json

json_string = '{"name " : "Aum", "age": 20, "city" : "Bangkok"}'


python_dict = json.loads(json_string)


# result is a py dictionary

print(python_dict["name "])
print(python_dict["age "])
print(python_dict["city "])
