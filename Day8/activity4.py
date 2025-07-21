fruit_prices={"elppa":100,
              "ananab":60,
              "egnaro":80}
print(fruit_prices[input("Enter fruit name:").lower()[::-1]])