import json
with open("authors.json") as f:
    data = f.read()

json_dict = json.loads(data)
print("The JSON document is loaded as type {0}\n".format(type(json_dict)))
print("Now printing each item in this document and the type it contains")
for k, v in json_dict.items():
 print("-- The key {0} contains a {1} value.".format(str(k), str(type(v))))