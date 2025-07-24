# list=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]] #existing list
# intersection = list(set.intersection(*map(set, list)))
# print(intersection)

# a={1,2,3}
# b={1,2,3,4,5}
# c={1,2}
# # print(a.issubset(b)) #True
# # print(c<=a) #True
# # print(a<b)
# # print(c<a)
# # print(c<=a)
# x={}

a={{1,2,3}:"hi"}
e={frozenset([1,2,3]):"hi"}
f={{1,2},{3,4}}
g={frozenset([1,2]),frozenset([3,4])}
print(e)