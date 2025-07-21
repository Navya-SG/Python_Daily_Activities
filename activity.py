#
v1=2
v2=type(int)
v3=3
print(v1,v2,v3)

#
print(type(v1),v2)

#
print(print())

#
v1=(1,3,6)
a,b,c=v1
print(a,b,c)



# numbers=tuple(input("enter number:"))
# *a, = numbers.strip()
# print(type(numbers))
# print(a)
'''
v1=tuple(1,2,3,4,5)
*a,= v1
print(len(a))
print(a)
print(type(a))'''

num=(1,2,3,4,5,6)
first,*middle,last=num
print(first,middle,last)

num=(1,2,3,4,5,6)
first,*middle,last=num
print(type(first),middle,last)