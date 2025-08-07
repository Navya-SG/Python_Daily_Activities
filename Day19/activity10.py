quote=input("Enter your inspiring quote:")
with open("quote.txt","a") as file:
    file.write(quote+"\n")
print(open("quote.txt").read())