# fruit_prices = {"elppa": 100,
#                 "ananab": 60,
#                 "egnaro": 80}  

# fruit_name = "".join(sorted(input("Enter fruit name: ")))
# keys = map("".join,map(sorted,fruit_prices.keys()))
# values = fruit_prices.values()
# updated_dict={keys==fruit_name:values}
# print(updated_dict)


# fruit_prices = {"elppa": 100,
#                 "ananab": 60,
#                 "egnaro": 80}  

# updated_prices = {
#     ''.join(sorted("elppa")): 100,
#     ''.join(sorted("ananab")): 60,
#     ''.join(sorted("egnaro")): 80,
# }

# fruit_name = input("Enter the fruit name: ")
# sorted_name = ''.join(sorted(fruit_name))
# price = updated_prices.get(sorted_name, "Fruit not found")

# print(price)



fruit_prices = {"elppa": 100, 
                "ananab": 80, 
                "egnaro": 60}
fruit_name = ''.join(sorted(input("Enter fruit name:")))
updated_fruit_prices = {''.join(sorted("elppa")): fruit_prices["elppa"],
          ''.join(sorted("ananab")): fruit_prices["ananab"],
          ''.join(sorted("egnaro")): fruit_prices["egnaro"]}
print(updated_fruit_prices.get(fruit_name, "not found"))




