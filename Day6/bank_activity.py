#account_info=name,acc_no,pan card,balance,credit,debit
acc_info=("Navya","1XXXX","AX123",2500.50,2000,100)
print(*acc_info)
print("Navya Sathishkumar",*acc_info[1:])

acc_info=("Navya","1XXXX","AX123",2500.50,2000,100)
print(*acc_info)
print(*acc_info[1:4],acc_info[4]+100,acc_info[5])

acc_info=("Navya","1XXXX","AX123",2500.50,2000,200)
debit = int(input("Enter amount to debit:"))
print(*acc_info)
print(*acc_info[:3],acc_info[3]-debit,acc_info[4],acc_info[5]-debit)

