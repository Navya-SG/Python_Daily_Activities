#
s1={1,2,3}
s2={1,2,3}
print(id(s1),id(s2)) #diff

#
s={1,2,[3,4],"hello"}
print(s) #error(list)

s={1,2,(3,4),"hello"}
print(s) #{1, 2, 'hello', (3, 4)} tuple

s={2,True,"hello"}
print(s) #{1, 2, 'hello'} bool(but only if 1 is not gives, True=1 so removes dict, same for false/0)

s={1,2,True,"hello", 2+4j }
print(s) #{1, 2, 'hello', (2+4j)} complex

s={1,2,True,"hello", 2+4j ,None}
print(s) #{None, 1, 2, (2+4j), 'hello'} None

s={1,2,True,"hello", 2+4j, None, {1:2,2:3}}
print(s) #error(dict)

s={1,2,True,"hello", 4.03, 2+4j ,None}
print(s) #{None, 1, 2, 4.03, 'hello', (2+4j)} float

s={1,2,{1,2}}
print(s) #error(set)

#
word=set('programming')
print(word)
print(len(word)) #8

#
word=set('programming',{'programming'})
print(word)
print(len(word)) #error

#
word=set('programming,programming')
print(word)
print(len(word)) #9

#set
fruit={'apple','banana','orange'}
fruit.update({'orange','pine'})
print(fruit)

#
fruits={'apple','mango','orange'}
fruits.remove('grape') #shows error
fruits.discard('grape') #prints fruits
fruits.pop() #removes randomly
fruits.clear() #empty set()
print(fruits)

#
fruits={'apple','mango','orange'}
print('apple' in fruits) #True

fruits={'apple','mango','orange'}
print('apple' not in fruits) #False

fruits={'apple','mango','orange'}
print({'apple' not in fruits,'mango' in fruits}) #ot in set

#
s=set("banana")
print(len(s)) #3

#
s={1,2,3}
s.add((4,5))
print(len(s)) #4

#
s={'a','b'}
s.update('cd',['e','f'])
print(sorted(s)) #['a', 'b', 'c', 'd', 'e', 'f']

#
s=set()
print(s.pop()) #error

#
s={'x','y','z'}
s.discard('a')
print(len(s)) #3

#
s=set()
s.update([1],(2,),{3})
print(len(s)) #3

#
a=set([1,2,3])
b=set([3,4,5])
a.update(b.intersection(a),b.difference(a))
print(len(a)) #5

#
a={1,2}
b=a
a.clear()
print(b) #set()

#
s={'x'}
s.add('x')
s.add('x')
print(len(s)) #1

#
set1={1,2,3}
set2={4,5,6}
union=set1|set2
print(union) #{1, 2, 3, 4, 5, 6}

#

