# d={1:'a', 2: 'b'}
# print(d.keys)

fruit_prices={"elppa":100,
              "ananab":60,
              "egnaro":80}
print(fruit_prices[input("Enter fruit name:").lower()[::-1]])
