data = {'a':1,'b':2,'c':1}
rev = {}
for k,v in data.items():
    rev.setdefault(v, []).append(k)
rev = {k: tuple(v) for k,v in rev.items()}
print(rev)
