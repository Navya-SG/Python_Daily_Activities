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


#
numbers=tuple(input("enter number:"))
*a, = numbers.strip()
print(type(numbers))
print(a)

#
v1=tuple(1,2,3,4,5)
*a,= v1
print(len(a))
print(a)
print(type(a))

#
num=(1,2,3,4,5,6)
first,*middle,last=num
print(first,middle,last)

num=(1,2,3,4,5,6)
first,*middle,last=num
print(type(first),middle,last)

#
players = {1:"dhoni", 2:"kholi", 3:"ashwin"}
print(players[1])

players = {"name":"dhoni" , "age":20}
print(players.get("email", "invalid"))

#
students = {"name":"navya",
            "name" : "navi"}
print(students)

#
d={1:'A', True:'B', 1.0:'C'}
print(d) #O.T: 1:'C'

#
a=dict([(1,2),(3,4)])
b=dict([(5,6),(7,8)])
c=dict([(1,2,3)])
d=dict([(1,2)])
print(type(a),type(b),type(c),type(d)) #error (c)

#
d=dict()
d[None]='empty'
print(d)  #OT:{None:'empty'}

