def f(x,lst=()):
    lst = list(lst)
    lst.append(x)
    return lst
print(f(1))  
print(f(2)) 
