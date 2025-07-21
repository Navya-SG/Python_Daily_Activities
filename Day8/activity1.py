#assign value to variables a,b,c
a=10
b=20
c=30
a,b,c=c,a,b #reassign values of a,b,c
print(a,b,c) #print a,b,c

a=10
b=20
c=30
a,b,c=(c,a,b)
print(a,b,c)

a=10
b=20
c=30
a,b,c=[c,a,b]
print(a,b,c)


a=10
b=20
c=30
a,b,c=[30,10,20]
print(a,b,c)


a=10
b=20
c=30
a,b,c=(30,10,20)
print(a,b,c)


a=10
b=20
c=30
a,b,c=(c,a,b)
print(a,b,c)
