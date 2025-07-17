data = "Luna42Kai3.14True#Knight"
a=data[:4].upper()
b=int(data[4:6])
c=float(data[9:13])
d=data[-1:-7:-1]
print("Name: "+a)
print(f"{b}+8={b+8}")
print(f"{c}*2={c*2}")
print("Reversed Title: " + d)