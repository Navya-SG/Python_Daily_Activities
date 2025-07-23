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