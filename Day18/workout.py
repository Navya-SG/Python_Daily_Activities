#find log values
import math
n = 100
log_value = math.log(n)
print(log_value)  

#
multiply = lambda x,y:x*y
print(multiply(5,2))

#
print(multiply(3,4) is 12)

#
val=int(input("enter a num:"))
square = lambda x:x**2
print(square(val))

#
val = int(input("Enter a number: "))
def find_lambda(val):
    square = lambda x: x ** 2
    print(square(val))
find_lambda(val)

#
sum = lambda x,y:sum(x,y)
print(sum(3,4)) #error

#
f = lambda:42
print(f()) #42

#
f = lambda x:(x+2,x*2)
print(f(3)) #(5,6)

#
sum = lambda x:x+2,#x*2
print(sum(3)) #error

#
lst=[1,2,3,4]
res=list(map(lambda x: x**2,lst))
print(res) #[1, 4, 9, 16]

#
lst=(1,2,3,4,5)
res=list(map(lambda x: x**2,lst))
print(res) #[1, 4, 9, 16, 25]

#
lst=(1,2,3,4,5,6,7,8,9,10)
res=list(filter(lambda x: x%2==0,lst))
print(res) #[2, 4, 6, 8, 10]

#
from functools import reduce
lst=(1,2,3,4,5)
res=reduce(lambda x,y: x*y,lst)
print(res) #120

#
lst = [1, 2, 3, 4, 5]
res = [x**2 if x%2!=0 else x**3 for x in lst]
print(res)

#
lst = [x*x for x in range(10)]
print(lst)

#
lst = []
for num in range(11):
    if num%2!=0:
        lst.append(num*num)
print(lst)

#
lst = []
for num in range(2, 11):
    for i in range(2, int(num**0.5) + 1):
        if num%i!=0:
            lst.append(num)
    else:
            continue
print(lst)

#
lst=[]
for num in range(2,11):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            break
    else:
        lst.append(num)
print(lst)

#
lst = [num for num in range(2, 11) if all(num % i != 0 for i in range(2, int(num**0.5) + 1))]
print(lst)

#
pairs = [(x,y) for y in range(2) for x in range(3)]
print(pairs)

pairs = [(x,y) for y in range(3) for x in range(2)]
print(pairs)

#
[i for i in range(5) if i * 0] #[]

#
odd={x: x**0.5 for x in range(10) if x%2==1}
print(odd)

#list of tuple to create dict
data=[('a',1),('b',2),('c',3)]
print({k:v for (k,v) in data}) #{'a': 1, 'b': 2, 'c': 3}

#
data=[('a',1),('b',2),('c',3)]
print({k:v for (v,k) in data}) #{1: 'a', 2: 'b', 3: 'c'}

#
lst = ['one','two','three','four','five']
indexed_dict = {i: lst[i] for i in range(len(lst))}
print(indexed_dict)

#
coords = {(x,y,z):x*y*z for x in range(2) for y in range(2) for z in range(2)}
print(coords)

#
n=[1,2,3,4,5,6]
r={i%2 for i in n}
print(r) #{0,1}

#
sq=(x*x for x in range(5))
print(sq)
print(next(sq))
print(list(sq))
# <generator object <genexpr> at 0x000001D793A8B440>
# 0
# [1, 4, 9, 16]

#
try:
    v1=int(input("enter integer:"))
except ValueError:
    v1=int(input("you'r entered input is wrong,kindly enter a integer:"))
print(v1)

