#
x="global"
def outer():
    def inner():
        print(x)
    x="enclosing"
    return inner
f=outer()
f()#enclosing

#
def gen_odd(num):
    n=0
    while n<=num:
        if n%2==1:
            yield n
        n += 1
odd_num=gen_odd(10)
for i in odd_num:
    print(i) #1 3 5 7 9

#
def greet():
    """navya function"""
    return("navya")
print(greet.__doc__)
