#
t1=tuple([1,2,3])
t2=1,2,3
t3=(1,2,3)
print(t1,t2,t3)

#
nested=((1,2),(1,2),(1,2))
print(nested)

#t1=1,2,3
t2="a","b"
t3=t1+t2
print(t3)

t1=1,2,3
t2="a","b"
t3=(t1+t2)*3
print(t3)

#
t1=(5,10,15,20,25)
t2=len(t1)-1
print(t2)

#
t1=(1,2,3,2)
print(t1.index(2))


####
t1=(1, 2, 3, 2)
t2=t1.index(2)
t3=len(t1)-1  #4-1=3
t4=t1[::-1].index(2) #2,3,2,1  3-0=3
t5=t3-t4 
print(t2, t5)

t1=(1, 2, 3, 2)
t2=t1.index(2)
t4=t1[1:]+t1[:1] #2,3,2,1  3-0=3
print(t4)

#
t1=(15,22,5,10)
print(min(t1)>max(t1))

#
x=(99,101,42,67)
print(min(x+(10,)))

#
x=(99,101,42,67,99)
print(x.count(99))

#
t1=(1,2,3,4)
t2=list(t1)
t2[1]=0
print(tuple(t2))

#
t=(10,20,30,40,50)
print("avg",sum(t)/len(t))

#
t=tuple(map(float,(input().split())))
print(int(sum(t))/len(t))

#account_info=name,acc_no,pan card,balance,credit,debit
acc_info=("Navya","1XXXX","AX123",2500.50,2000,100)
print(*acc_info)
print("Navya Sathishkumar",*acc_info[1:])

acc_info=("Navya","1XXXX","AX123",2500.50,2000,100)
print(*acc_info)
print(*acc_info[:3],2500.50-100,2000,100-100)

acc_info=("Navya","1XXXX","AX123",2500.50,2000,100)
print(*acc_info[:5],0)
