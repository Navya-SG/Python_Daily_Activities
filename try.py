#ones/twos complement, binary operators

list1=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]
set1,set2,set3,set4=set(list1[0]),set(list1[1]),set(list1[2]),set(list1[3])
common = list(set1.intersection(set2).intersection(set3).intersection(set4))
print(common)
