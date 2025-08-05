def armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    total = sum(d ** power for d in digits)
    return total == n
print(armstrong(153))  
print(armstrong(123)) 
