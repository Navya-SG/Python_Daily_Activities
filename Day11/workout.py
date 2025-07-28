a={1,2,3}
b={2,3,4}
print(len(a|b)) #4

# x=set("abc")
# y=set("bcd")
# print(sorted(x&y)) #b

s1={1,2,3}
s2={3,4,5}
s1.symmetric_difference_update(s2)
print(sorted(s1)) #[1,2,4,5]

x=set()
y={1,2}
z=x^y
print(type(z),len(z)) #<class 'set'> 2

a={1,2,3}
b=a
a|={4}
print(a)
print(len(b)) #4

a={1,2,3}
b={1,2,3,4,5}
c={1,2}
print(a.issubset(b)) #True
print(c<=a) #True

a=set("abc")
b={'a','b'}
c={'a','b','c'}
print(b.issubset(a) and a.issubset(c)) #true

a=set()
b={frozenset()}
c={frozenset(),frozenset({1})}
print(b.issubset(c)) #True

a={{1,2,3}:"hi"}
e={frozenset([1,2,3]):"hi"}
f={{1,2},{3,4}}
g={frozenset([1,2]),frozenset([3,4])}
print(e)


a={1,2,3}
b={1,2,3,4,5}
c={1,2}
print(a.issubset(b)) #True
print(c<=a) #True
print(a<b)
print(c<a)
print(c<=a)
x={}

list=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]] #existing list
intersection = list(set.intersection(*map(set, list)))
print(intersection)
