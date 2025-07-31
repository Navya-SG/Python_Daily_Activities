val = [29,10,14,37,13]
for i in range(len(val)):
    min = i
    for j in range(i+1,len(val)):
        if val[j]<val[min]:
            min = j
    val[i],val[min]=val[min],val[i]
print("sorted list:",val)
















'''
if values[0] > values[1]:
	values[0],values[1]=values[1],values[0]
	print(values)
if values[1] > values[2]:
	values[1],values[2]=values[2],values[1]
	print(values)
if values[2] > values[3]:
	values[2],values[3]=values[3],values[2]
	print(values)
'''