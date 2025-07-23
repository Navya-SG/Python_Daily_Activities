students={'Alice','Bob','Charlie'}
new_entries = ['Charlie','Diana','Eve','Bob','Frank']
bef_add=len(students)
# print(bef_add)
students.update(new_entries)
#print(students)
aft_add=len(students)
# print(aft_add)
print("Number of names added:",aft_add-bef_add)
