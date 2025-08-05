data=[('Alice',90),('Bob',75),('charlie',90),('Dave',60)]
sort_data = sorted(data, key = lambda x: (-x[1],x[0]))
print(sort_data)