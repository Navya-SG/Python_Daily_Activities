number = int(input())
count = 0
while number>=0:
	number-=3
	count+=1
print("loop runs times:",count)

#using for_1
number = int(input())
count = 0
for i in range(0,number+1,3):
    count += 1
print("loop runs times:", count)

#using for_2
number = int(input())
count = 0
for i in range(1,number+1):
	if number > 0:
		number -= 3
		count+=1
print("loop runs times:",count)
