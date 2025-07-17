#find greater number
#sol1
a = 10
b = 5
print("a is bigger than b - the statement is", bool(a>b))

#sol2
a = 10
b = 5
print("Greater number is:", a - ((a-b) * (a-b)) // ((a-b) * (a-b) + 1) * (a-b))
