a,b = map(int,(input("Enter two numbers:")).split(" ")) #0010 2 0011 3
a = a ^ b #0001 1
b = b ^ a #0010 2
a = a ^ b #0011 3
print(a,b)

