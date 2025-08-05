data = [[1,2,None],[],[3,'',4],[0,5,5],[None,6]]
flat = (x for x in data for x in x if x)
data_upd = set()
result = [x for x in flat if not (x in data_upd or data_upd.add(x))]
print(result)
