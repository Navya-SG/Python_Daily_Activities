access_data={(100,209):"Alice",
            (104,210):"Bob",
            (105,211):"Charlie",
            (106,212):"Diana"}
swap_data=dict(zip(access_data.values(),access_data.keys()))
print(swap_data)

reversed_data = dict(reversed(access_data.items()))
print(reversed_data)

reversed_swap_data = reversed(swap_data)
print(reversed_swap_data)






