find = int(input())
values = [10, 25, 67, 42, 92]
values.sort()  #10 25 42 67 92
min = 0
max = len(values) - 1
while min <= max:
    mid = (min + max) // 2
    if values[mid] == find:
        print("Value found at index:", mid)
        break
    elif find > values[mid]:
        min = mid + 1
    else:
        max = mid - 1
else:
    print("Value not found")

'''

find = int(input())
values = [10, 25, 67, 42, 92] #10 25 42 67 92
values.sort()
mid = values[len(values)//2]
#print(mid,values[(len(values)//2)+1])
if find == mid:
	print("value found at index:",len(values)//2)
	break
elif find > mid:
	list=[]
	list+=[values[mid]:]
	m = list[len[list]//2]'''





