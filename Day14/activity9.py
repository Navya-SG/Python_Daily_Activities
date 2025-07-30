#
value =input("Enter a number:")
if value[-1] in ["1","3","5","7","9"]:
	print("Odd")
else:
	print("Even")

#final sol
value =input("Enter a number:")
if value & 1:
	print("Odd")
else:
	print("Even")