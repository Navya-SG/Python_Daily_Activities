# reverse the dict
access_data={(100,209):"Alice",
            (104,210):"Bob",
            (105,211):"Charlie",
            (106,212):"Diana"}
swap_data=dict(zip(access_data.values(),access_data.keys()))
print(swap_data)

reversed_data = dict(reversed(access_data.items()))
print(reversed_data)

reversed_swap_data = dict(reversed(swap_data.items()))
print(reversed_swap_data)

#
students={'Alice','Bob','Charlie'}
new_entries = ['Charlie','Diana','Eve','Bob','Frank']
combine=list(students) + new_entries #students + new_entries
print(*set(students),*set(new_entries))

#
students={'Alice','Bob','Charlie'}
new_entries = ['Charlie','Diana','Eve','Bob','Frank']
combine=list(students) + new_entries #students + new_entries
print(set(students),set(new_entries))




