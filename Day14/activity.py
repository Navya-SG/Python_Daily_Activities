'''#activity7
val1,val2=map(int,input().split(" "))
if val1%val2==0:
	print(max(val1,val2))
else:
	print(val1+val2)

#activity8
val=input()
if val[0]+val[1]==val[2]+val[3]:
	print("Lucky")
else:
	print("Unlucky")

#activity9
val=input()
if val[-1] in ["1","3","5","7","9"]:
	print("Odd")
else:
	print("Even")

#activity10
string1,string2=map(str,input().split(" "))
if string1==string2:
	print("Match")
else:
	print("No Match")

#activity11
int(input())==42 and print("Magic")

#activity12
numbers = input().split(" ")
if numbers == sorted(numbers):
	print("Ascending")
elif numbers == sorted(numbers)[::-1]:
	print("Descending")

#activity13
val=int(input())
if val in range(10,20):
	print("within range")

#activity15
val1,val2=map(int,input().split(" "))
if (val1%2==0 and val2%2!=0) or (val2%2==0 and val1%2!=0):
	print("Exactly one is odd")

#activity17
val=input()
rev=val[::-1]
if val == rev:
	print("Mirror")
else:
	print("Broken")


#activity16
bln1=input()
bln2=input()
bln3=input()
#al = int(bool(bln1))+int(bool(bln2))+int(bool(bln3)) 
if bln1+bln2+bln3 == 1:
	print("Exactly one") 
#al!=1 and print("None")'''

#activity14
val=input()
if bool(val):
	print("Truthy")
elif bool(val) == False:
	print("Falsy")

	
















