values = [10,25,67,35,42]
search_val=int(input("Enter the value to search:"))
for i in range(len(values)):
	if values[i] == search_val:
		print("Found the value at index of:",i)
		break
else:
    print("Value not found")
