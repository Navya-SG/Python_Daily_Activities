#
name=input()
if name:
    print(f"hello,{name}!")
else:
    print("name is empty")

#
age=int(input())
if name:
    print(f"hello,{name}!")
else:
    print("name is empty")


#
age=20
if age>=18 and input():
    print("eligible")

#
print(True or False and False) #True

#
age=17
has=True
mem=True
if (age>=18 and has) or mem:
    print("entry")
else:
    print("no") #entry

#
if 0 and 10/0:
    print("math passed")
else:
    print("not passed") #not passed

#Ternary operator
age=20
status="Adult" if age>=18 else "minor"
print(status) #Adult

#
data=[]
print(all(data),any(data)) #True False

#
data=["",[],0,None]
print(all(data),any(data)) #False False

#
x=0
if x == x == x == x == x:
    print("Python")

#
if [] == False:
    print("A")
if not []:
    print("B") #B


