num = int((x := input("Enter the number: ")).isdigit()*x or input("Kindly enter numeric value: "))
print((num%3==0 and num%5==0 and num%7==0 and "jugsmugspugs") or (num%3==0 and num%5==0 and "jugsmugs") or  (num%3==0 and num%7==0 and "jugspugs") or  (num%5==0 and num%7==0 and "mugspugs") or (num%3==0 and "jugs") or (num%5==0 and "mugs") or (num%7==0 and "pugs") or x)
