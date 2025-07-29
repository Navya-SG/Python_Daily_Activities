val1,val2=map(int,input().split(" "))
if (val1%2==0 and val2%2!=0) or (val2%2==0 and val1%2!=0):
	print("Exactly one is odd")