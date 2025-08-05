func = [lambda i=i: i * 3 for i in range(1,4)]
print([f() for f in func])
