#
string1,string2=map(str,input("Enter two strings:").split())
if string1==string2:
	print("Match")
else:
	print("No Match")

#final sol
string1,string2=map(str,input("Enter two strings:").split())
if string1.lower()==string2.lower():
	print("Match")
else:
	print("No Match")