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


'''
reversed dict (keys,values)?
how to keep/store ordered value in set
how to store duplicates in set
scrambled - membership
walrus - dict
'''

original_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = dict(zip(original_dict.values(), original_dict.keys()))
print(reversed_dict)


values = ['banana', 'apple', 'banana', 'cherry']
ordered_set = set(dict.fromkeys(values))
print(ordered_set)

values = {'banana', 'apple', 'banana', 'cherry'}
ordered_set = tuple(values)
print(ordered_set)

from collections import Counter
values = ['apple', 'banana', 'apple', 'cherry']
counter = Counter(values)
print(counter)  # Output: Counter({'apple': 2, 'banana': 1, 'cherry': 1})

duplicate_set = {'apple'*2, 'banana'*1, 'cherry,'*3}
print(duplicate_set)

a={'a':[1],
   'b':{2},
   'a':{c}}
print(a)

