#
value=input("Enter 4 digit number:")
if value[0]+value[1]==value[2]+value[3]:
	print("Lucky")
else:
	print("Unlucky")

#final sol
value=input("Enter 4 digit number:")
if len(value)==4 and value[0]+value[1]==value[2]+value[3]:
	print("Lucky")
else:
	print("Unlucky")