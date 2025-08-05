def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
def next_prime(N):
    for num in range(N+1,1001):
        if is_prime(num):
            return num
    return "Not found"
print(next_prime(997))
