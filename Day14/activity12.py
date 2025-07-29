numbers = int(input("Enter numbers:").split(" "))
if numbers==sorted(numbers):
	print("Ascending")
elif numbers==sorted(numbers)[::-1]:
	print("Descending")