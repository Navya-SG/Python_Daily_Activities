quote=input("Enter your inspiring quote:")
with open("quote.txt","w") as file:
    file.write(quote)
print(open("quote.txt").read())
