#account_info=name,acc_no,pan card,balance,credit,debit
acc_info=("Navya","1XXXX","AX123",2500.50,2000,100)
print(*acc_info)
print("Navya Sathishkumar",*acc_info[1:])

acc_info=("Navya","1XXXX","AX123",2500.50,2000,100)
print(*acc_info)
print(*acc_info[:3],2500.50-100,2000,100-100)

acc_info=("Navya","1XXXX","AX123",2500.50,2000,100)
print(*acc_info[:5],0)