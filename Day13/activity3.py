grade_dict={
    "A":"Excellent work!",
    "B":"Good job!",
    "C":"Satisfactory",
    "D":"Needs improvement",
    "F":"Please study more"}
score = int(input("enter score:"))
if score>=90:
    grade = "A"   
elif score>=80:
    grade = "B"   
elif score>=70:
    grade = "C"   
elif score>=60:
    grade = "D"   
else:
    grade = "F"   
print(f"Grade :{grade},", grade_dict.get(grade))