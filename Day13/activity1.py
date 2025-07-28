# marks = int(input("enter marks out of 100:"))
# cutoff=int(input("enter cutoff mark:"))
# if (marks - cutoff) :
# 	print("pass")

#final sol
marks = int(input("enter marks out of 100:"))
cutoff = int(input("enter cutoff mark:"))
if (marks-cutoff + abs(marks-cutoff)) // 2 is (marks-cutoff):
    print("pass")