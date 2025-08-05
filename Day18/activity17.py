try:
    inp=int(input())
    check = lambda x: x if x % 2 == 0 else x.throw(ValueError("Number is odd"))
    print(check(inp))
except:
    print("Its a odd number")