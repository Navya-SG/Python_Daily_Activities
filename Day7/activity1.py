num = int((x := input("Enter the number: ")).isdigit()*x or input("Kindly enter numeric value: "))
print((num % 3 == 0 and "jugs") or x)