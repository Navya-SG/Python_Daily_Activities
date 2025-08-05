data=[1,2,3,4,5,6,7,8,9]
try:
    index=int(input("Enter index:"))
    print(data[index])
    print("Found")
except IndexError:
    print("Out of bounds")
