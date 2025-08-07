import json
json_data='[{"name": "June", "email": "june@example.com"},{"name": "Alex", "email": "alex@example.com"},{"name": "June", "email": "june@example.com"},{"name": "Dane", "email": "dane@example.com"}]'

py_data = json.loads(json_data)
unique = []
duplicates = []
for item in py_data:
    if item not in unique:
        unique.append(item)
    else:
        duplicates.append(item)
print(unique)
print(duplicates)
