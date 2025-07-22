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

'''fruit_prices = {"elppa": 100,
                "ananab": 60, 
                "egnaro": 80}  
   sorted_fruits={"apple":fruit_prices.get"elppa",
                
fruit_name = "".join(sorted(input("Enter fruit name: "))) 
sorted_keys = "".join, map(sorted, fruit_prices.keys())
print(fruit_name in sorted_keys and fruit_prices.get(fruit_name,"None"))''' 