'''Given a list of numbers, extract every 3rd element starting from index 1, reverse it, then combine it with every 2nd element from the original list starting from index 0. Finally, multiply the entire result by 2.
 
IP:
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
 
op:
[80, 50, 20, 10, 30, 50, 70, 90, 80, 50, 20, 10, 30, 50, 70, 90]'''



numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
extract = numbers[1::3]  
reverse = extract[::-1] 
num2=numbers[0::2] 
combine=reverse+num2 
output=combine*2 
print(output)




 

