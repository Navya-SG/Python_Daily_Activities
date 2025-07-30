#
val1,val2=map(int,input("Enter numbers:").split(" "))
if val1%val2==0:
	print(max(val1,val2))
else:
	print(val1+val2)

# final sol
val1,val2=map(int,input("Enter numbers:").split(" "))
if val1!=0 and val2%val1==0:
	print(val2)
elif val2!=0 and val1%val2==0:
	print(val1)
else:
	print(val1+val2)