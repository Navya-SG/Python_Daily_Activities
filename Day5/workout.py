#activity 1
x=426
middle=str(x)
print("Middle digit is: " + middle[1])

#input = input()
#output = print()
a=int(input("Enter a number:"))
print("Output is:",a + 5)

#/n
print("Hello, \nWorld!")

#date
print("2025", "07", "16", sep="-")

#print: 5-->4-->3-->2-->1-->Liftoff!
print(5,4,3,2,1,"Liftoff!", sep = "-->")

#split() 2 no's
x,y=input("enter 2 no's: ").split()
print(x,y)

#3split()  no's
x,y,z=input("enter 3 no's: ").split()
print(x,y,z)

#2 no's
x,y=input("enter 2 no's: ").split(',')
print(x,y)


#multiple datatype input in same line
x,y=int(input("enter no1: ")),float(input("enter no2: "))
print(x,y)

#
letters=list("hello")
print(letters[0].upper(),letters[1].upper(),letters[2].upper(),letters[3].upper(),letters[4].upper())

#unpacking
print(*list('hello'.upper()))

# lower -> upper
name=list("hello")
for char in name:
    print(chr(ord(char) - 32), end="")

#
words = ["greek","for","geeks"]
for word in words: #greekforgeeks
    for letter in word: #g r e e k f o r g e e k s
        print(chr(ord(letter)-32),end="") # G R E E K F O R G E E K S
    print(" ",end="") #G R E E K  F O R  G E E K S

#
input=list(input("enter input:").split(','))
print(input[::2])

#
guests = ["Anita","Rahul","Kiran","Meera"]
print(guests[0][0])

#
numbers=[123,287,9001]
print(str(numbers[2]))

#
'''get user name
input should be in lower case
convert to upper without using string.upper'''

name = input("Enter your name:")
name_str = name.lower()
print(chr(ord(name_str)-32))

#
input=list(input("enter input:").split(','))
print(*input[::2])

#1
name=["alice","bob","charlie"]
print(name[0].index('i'))

#2
input=[123,287,9001]
input_str=str(input[2]) #9001
input_str=input_str[:2] + '3' + input_str[3:] 
input[2] = int(input_str)
print(input)

#3
a=[1,2]
b=[3,4]
c=[5,6]
a.extend(b)
a.extend(c)
print(a)


#4 remove all duplicates
num=[1,2,3,2]
for n in num:
    num.remove(2)
print(num)

fruits=["apple","banana","orange","banana"]
for fruit in fruits:
    fruits.remove("banana")
print(*fruits)