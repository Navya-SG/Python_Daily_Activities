access_data={(100,209):"Alice",
            (104,210):"Bob",
            (105,211):"Charlie",
            (106,212):"Diana"}
key=tuple(map(int,input("enter key:").split(',')))
print(access_data.get(key) or access_data.get(key[::-1]) or "key not match")