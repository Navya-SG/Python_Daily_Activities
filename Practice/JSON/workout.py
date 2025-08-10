dump - python to json
load - json to python

dump - python data into json file,w
dumps - python dict to json
load - read json file and convert to python dict,r
loads - json string to python dict


# create json file and add data to it (py -> json file)
import json
data = {"name": "Navya", "role": "Engineer"}
with open("data.json","w") as f:
    json.dump(data,f)

# convert python dic to json data (py -> json data)
import json
data = {"name": "Navya", "role": "Engineer"}
x = json.dumps(data)
print(x) #{"name": "Navya", "role": "Engineer"}

# convert json string to python dict (json string -> py)
import json
data = '{"name": "Navya", "role": "Engineer"}'
x = json.loads(data)
print(x) #{'name': 'Navya', 'role': 'Engineer'}

# reads data from json file and convert to python dict (json data -> python)
import json 
with open("data.json","r") as f:
    data=json.load(f)
    print(data) #{'name': 'Navya', 'role': 'Engineer'}

#access data
import json
data = '{"name": "Navya", "role": "Engineer"}'
x = json.loads(data)
print(x["name"])

#act1
import json
data={"city":"paris","temp":21}
x = json.dumps(data)
print(x)

#act2
import json
data='{"product":"book","price":9.99}'
x = json.loads(data)
print(x["product"],x["price"])

#act3
import json
data='{"name": "June", "contact": {"email": "june@example.com","city": "Paris"}}'
x = json.loads(data)
print("Email:",x["contact"]["email"],"City:",x["contact"]["city"])

#act4
import json
data={"user":"alex","active":True}
with open("user.json","w") as f:
    json.dump(data,f)
with open("user.json","r") as jf:
    x = json.load(jf)
if x["active"]:
    print("User is active.")
else:
    print("User is not active.")

#act5
import json
try:
    with open("missing.json","r") as f: 
        print(json.load(f))
except FileNotFoundError:
    print("File not found")

#act6
