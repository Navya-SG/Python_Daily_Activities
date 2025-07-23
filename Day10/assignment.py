list1=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]] #existing list
print(list(set(list1[0]).intersection(set(list1[1])).intersection(set(list1[2])).intersection(set(list1[3])))) #find common numbers in all set as list and print 
