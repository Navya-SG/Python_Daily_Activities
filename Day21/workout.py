#
'{"name":["Alice","Bob"],"Age":[30,25],"City":["New York","Bob"]}'

#
print("{}hello,{}!".format("Alice",42)) #Alicehello,42!
print("{n1} Hello, {n2}!".format(n2='Alice',n1=42)) #42 Hello, Alice!
print("{2} scored {0} marks in {1}".format(85,"Maths","Alice")) #Alice scored 85 marks in Maths
print("{%d} Hello, {%s}!" % (42, 'Alice')) #{42} Hello, {Alice}!

#
user="ravi"
score=87.5
print(f"{user=},{score=},{score/100=:.2%}") #user='ravi',score=87.5,score/100=87.50%