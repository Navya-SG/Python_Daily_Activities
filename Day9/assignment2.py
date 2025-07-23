data =[('A', 1, 2),
       ('B', 3),
       ('C', 4, 5, 6),
       ('D',),
       ('E', 7, 8)]
sorted_data = sorted(data, key=len)
result = list(list(zip(*sorted_data))[0])
print(result)
