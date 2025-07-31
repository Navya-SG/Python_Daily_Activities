#function
name=input()
def greet(name):
    print(f"hello, {name}!")
greet(name)

#return
n=int(input())
def check(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    return "Zero"
print(check(n))

#
def greet():
    return "Hello"
message = greet()
print(message)  # prints "Hello"

#
def stats(x,y):
    return x+y,x*y
print(stats(2,5))
print(type(stats(2,5)))
v1=stats(3,10)
print(v1,type(v1))

#
def stats_check(x):
	return x**x
print(stats_check(2),type(stats_check(2)))

#
def f(a, x=[]):
    x.append(a)
    return x
print(f(1));print(f(2))

#
def fun1():
    def fun2(name):
        return "Hello " + name.upper()  
    return fun2
res = fun1()
print(res("navya")) 

#
def fun(name):
        return "Hello " + name.upper()  
res = fun
print(res("navya"))

#
#def test():
#    return x = 5
#print(test()) #cannot assign value in return statement

#
def fun(x,y):
    return "hi"
print(fun(1)) #gives error

#
def fun(x,y):
    return x/y
print(fun(10,2)) #5.0

def fun(x,y):
    return x/y
print(fun(2,10)) #0.2

#
def fun(x,y): #x,y -> actual parameter
    return x/y
print(fun(x=10,y=2)) #x,y -> argument parameter
print(fun(x=2,y=10)) #x,y -> argument parameter

#
def fun(x,y): #x,y -> actual parameter
    return x/y
print(fun(x=10,y=2)) #x,y -> argument parameter
print(fun(2,x=10)) #error bcoz x=2 already

#
#def greet(time="morning", name): #error bcoz default parameter then only non-default parameter
#     print(f"good {time}, {name}!")
# greet("Alice")
# greet("bob","evening")

#
def greet(a,x=[]):
    x.append(a)
    return x
print(greet(1));print(greet(2)) #[1] [1,2]

#
def greet(a,x=[]):
    x += [a]
    return x
print(greet(1));print(greet(2,[]));print(greet(3));print(greet(4)) #[1] [2] [1,3] [1,3,4]

#
lia=[]
lib=[]
lic=lia
print(id(lia),id(lib),id(lic)) #a,c same,b diff

#
def total(*args):
    print(args)
    return sum(args)
print(total(2,-1,True))
print(total(10))
print(total()) #(2, -1, True) 2 (10,) 10 () 0

#
def foo(args):
    print("args:", args)
foo(1,2,3) #error

def foo(*args):
    print("args:", args)
foo(1,2,3) #args: (1, 2, 3)

#
def info(**kwargs):
    print(kwargs)
info(name="navya",age=18) #{'name': 'navya', 'age': 18}

#
def info(**kwargs):
    if "name" in kwargs:
        print("hi",kwargs["name"])
info(name="navya") #hi navya

#
def show(**kwargs):
    print(kwargs)
show ("name",age=30) #error only key is given for name,no value

#
def show(*args, **kwargs):
    print("[LOG]:",*args,**kwargs)
show ("HELLO","WORLD",sep="~",end="$$\n")  #[LOG]:~HELLO~WORKD$$

#
def info(id,*args,**kwargs):
    print(id)
    print(args)
    print(kwargs)
info(1,"navya",age=18)  #1 ('navya',) {'age': 18}

#
def lis(val,lst=[]):
    lst+=[val]
    return lst
v1=lis(1)
v2=lis(2,[])
v3=lis(3)
v4=lis(4)
print(f"v1:{id(v1),v1},v2:{id(v2),v2},v3:{id(v3),v3},v4:{id(v4),v4}")
#v1:(2810570432704, [1, 3, 4]),v2:(2810570581568, [2]),v3:(2810570432704, [1, 3, 4]),v4:(2810570432704, [1, 3, 4])

#