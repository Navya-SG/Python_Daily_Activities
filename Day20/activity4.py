# find a duplicate file
import json
json_data='{"name":"June","contact":{"email":"june@example.com","city":"Paris"}}'
py_file = json.loads(json_data)
print(py_file["contact"]["email"],py_file["contact"]["city"])


