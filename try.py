'''values = [10, 25, 67, 35, 42, 92]
values.sort()
search_val = 25
low = 0
high = len(values) - 1

while low <= high:
    mid = (low + high) // 2
    if values[mid] == search_val:
        print(f"Found {search_val} at index {mid} in sorted list")
        break
    elif values[mid] < search_val:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")
'''
