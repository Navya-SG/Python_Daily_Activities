raw_guests=["alice","","Bob","ALICE"," bob ", " Eve ","eve", " ","  ANAND"]
res= {x.strip().capitalize().strip() for x in raw_guests if x.strip()}
fin={x: len(x) for x in res}
print(fin)
