username=input("Enter username:")
password=input("Enter password:")
if username == "admin" and (password == "secret123" or password == "letmein"):
	print("Access permitted")
else:
	print("either of the credentials are invalid")