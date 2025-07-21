#
v1=(1,3,6)
a,b,c=v1
print(a,b,c)

#
tuple1=(1,2,3)
list=list(tuple1)
print(list)

#
tuple1=(1,2,3,4,5,6,7,8,9,10)
first,*middle,last=tuple1
print(first,middle,last)

#
dict={"id":1, "name":input("enter name:")}
print(dict)

#
students={"name":"navya",
          "age":14,
          "city":int(input("enter city :"))}
print(students)

#
students={"name":"navya",
          "age":14,
          "num":1}
students.pop("num")
print(students)

#
students={"name":"navya",
          "age":14,
          "num":1}
del students["num"]
print(students)

#
v1=int(input())
v2=int(input())
print(id(v1))
print(id(v2))
