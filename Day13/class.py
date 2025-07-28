#
data=set("hello")|set("world")
print(data) #{'r', 'e', 'l', 'd', 'h', 'w', 'o'}
print(len(data)) #7

#
a={1,2,3}
b={4,5,6}
c={frozenset([1,2])}
d={{1,2}}
print(a,b,c,d) #d raise error

#
print(False + True) #1

#
print(bool(0+1)) #1

#
v1=bool(1)
print(v1) #True

#
v2=bool(5)
print(v2) #True

#
v3=bool(False)
print(v3) #False

#
v4=bool(0)
print(v4) #False

#
v5=bool(5-5)
print(v5) #False

#
print(id(v1)==id(v2)) #True

#
print(id(v1),id(v2)) #same id

#
v6=True+True
print(v6) #2

#
v7=1+1
print(v7) #2

#
print(v6==v7) #True

#
v8=True
v9=1
print(id(v8)==id(v9)) #False

#
print(id(v8),id(v9)) #diff id

#
v10=int(True)
v11=int(1)
print(id(v10)==id(v11)) #True

# all the below are false
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(None))

#
a = 1
b = True
print(a,b)
print(id(a)==id(b)) #False

#
print(bool('False')) #True

#
a=5
b=5
print(a==b)
print(id(a)==id(b))
print(bool(a)==bool(b))
print((not bool(a)) == (not bool(b)))
print(type(a)==type(b))
print(float(a)==float(b))
print(id(float(a))==id(float(b)))
print(float(a)==float(b))
print((a and b) == (b and a))
print((a or b) == (b or a))
print( 5 == '5')
print('5' == '5')
x={}
y=[]
print(x==y)
z={0}
w=[0]
print(z==w)

#
print('5' > 3) #str 