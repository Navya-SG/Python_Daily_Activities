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

#sol
acc_info=("Navya","1XXXX","AX123",2500.50,2000,int(input("Enter amount to debit:")))
debit = acc_info[5]
print(*acc_info[:3],acc_info[3]-debit,*acc_info[4:])

#sol_fin
acc_info=("Navya","1XXXX","AX123",[int(input("Enter credited amount:")),2500.50,int(input("Enter debited amount:"))])
credit_history,current_balance,debit_history = acc_info[3][0],acc_info[3][1],acc_info[3][2]
result = current_balance+credit_history,current_balance-100,debit_history
print(*acc_info[:3],"credit_history:",result[0],"current_balance:",result[1],"debit_history:",result[2])



