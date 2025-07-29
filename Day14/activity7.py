val1,val2=map(int,input("Enter numbers:").split(" "))
if val1%val2==0:
	print(max(val1,val2))
else:
	print(val1+val2)