#
word='python'
for char in word:
    print(char, end="-")#p-y-t-h-o-n
#
students={"alice":95,"bob":88,"charlie":92}
for name in students:
    print(name)
for name,score in students.items():
    print(f"{name}:{score}") 
'''OT:
bob
charlie
alice:95
bob:88
charlie:92
'''
#
students={"alice","bob","charlie",1,2,3}
for name in students:
    print(name) #unordered

#
students={9,1,7,3}
for name in students:
    print(name) #same as given

#
numbers={8,3,7,1}
for num in numbers:
    print(num) #same as given

#
for i in range(2,2):
    print(i) #nothing

#
print(list(zip([1,2],['a','b','c']))) #[(1, 'a'), (2, 'b')]

#
for i in range(2):
    for j in range(3):
        if j==1:
            break
        print(j,end="") #00

#

'''
image 1 no b/t 100
max or min?
'''
'''
#
pwd=input("Enter a password:")
if len(pwd)>=8 :
	for i in pwd:
		if i == i.upper():
			
		elif i == i.lower():
		elif i.isdigit():
		elif not i.isdigit() and not i.isalpha()


for i in pwd:
	if i == i.lower()
'''

