'''read input from user
if string, you should check if given string is palindrome or not
if number, print the given num is odd or Even 
if num is float, print(len of number)
not all there, print not a valid type
dont use cond,loop
input - string'''

#solution 1
user_input = (x:=input("enter:"))
result1 = x.isdigit() and (int(user_input)%2==0 and "the number is even" or "the number is odd")
result2 = '.' in x and len(user_input)
result3 = x.isalpha() and x==user_input[::-1] and "Palindrome" or "Not Palindrome"
print(result1 or result2 or result3 or "not valid")

#condition
user_input = (x:=input("enter:"))
result2 = '.' in x and x.split(' ') and x.replace('.','') 
sol = result2.isalpha() or len(user_input)
print(sol)

#condition_simplified
user_input = (x:=input("enter:"))
print(('.' in x and x.replace('.','')).isalpha() or len(x))

#final solution (solution 1 + condition_simplified)
user_input = (x:=input("enter:"))
result1 = x.isdigit() and (int(user_input)%2==0 and "the number is even" or "the number is odd")
result2 = x.isalpha() and (x==user_input[::-1] and "Palindrome" or "Not Palindrome")
result3 = ('.' in x and x.replace('.','').isalpha()) or len(user_input)
print(result1 or result2 or result3 or "not valid")


