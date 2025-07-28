# marks = int(input("enter marks out of 100:"))
# cutoff=int(input("enter cutoff mark:"))
# if (marks - cutoff) :
# 	print("pass")

marks = int(input("enter marks out of 100:"))
cutoff = int(input("enter cutoff mark:"))
if ((marks - cutoff) // (abs(marks - cutoff) + 1)):
    print("pass")