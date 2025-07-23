#sol1
fruit_prices={"elppa":100,
              "ananab":60,
              "egnaro":80}
print(fruit_prices[input("Enter fruit name:").lower()[::-1]])

#sol2
fruit_prices = {
    "elppa": 100,
    "ananab": 60,
    "egnaro": 80,}

fruit_name = "".join(sorted(input("Enter fruit name: "))) #input from user
dict_keys = list(map(sorted,fruit_prices.keys())) #extracting dict keys alone
index = (fruit_name in dict_keys) and (dict_keys.index(fruit_name)) #check & acessing the index
list[fruit_name]==list[dict_keys] and print(fruit_prices.get(fruit_name))
key = dict_keys[index] #access index from list of keys

print(fruit_prices.get(key)) #print price

#sol3
fruit_prices = {"elppa": 100,
                "ananab": 60, 
                "egnaro": 80}  
fruit_name = "".join(sorted(input("Enter fruit name: "))) 
sorted_keys = list(map("".join, map(sorted, fruit_prices.keys())))  
print(fruit_prices.get(list(fruit_prices.keys())[sorted_keys.index(fruit_name)]))  

#sol4
fruit_prices = {"elppa": 100,
                "ananab": 60, 
                "egnaro": 80}  

sorted_fruits = {"apple":fruit_prices.get("elppa"),
                 "banana":fruit_prices.get("ananab"),
                 "orange":fruit_prices.get("egnaro")}

fruit_name = input("Enter fruit name: ") 
print(sorted_fruits.get(fruit_name,"None"))

#sol5
fruit_prices = {"elppa": 100, 
                "ananab": 80, 
                "egnaro": 60}

fruit_name = ''.join(sorted(input("Enter fruit name:")))

updated_fruit_prices = {''.join(sorted("elppa")): fruit_prices["elppa"],
                        ''.join(sorted("ananab")): fruit_prices["ananab"],
                        ''.join(sorted("egnaro")): fruit_prices["egnaro"]}

print(updated_fruit_prices.get(fruit_name, "not found"))

#final solution
fruit_prices = {
    "elppa": 100,
    "ananab": 60,
    "egnaro": 80,}
fruit_name = ''.join(sorted(input("Enter fruit name: "))) # Get input and sort
sorted_keys = dict(zip(list(map("".join, map(sorted, fruit_prices.keys()))),fruit_prices.values())) #extract keys,sort and store in new dict
print(sorted_keys.get(fruit_name, "Fruit not found")) #print the price

#FINAL SOLUTION PRO
fruit_prices = {
    "elppa": 100,
    "ananab": 60,
    "egnaro": 80,}
sorted_dict = dict(zip(list(map("".join, map(sorted, fruit_prices.keys()))),fruit_prices.values())) #extract keys,sort and store in new dict
print(sorted_dict.get(''.join(sorted(input("Enter fruit name: "))), "Fruit not found")) # get input and print the price