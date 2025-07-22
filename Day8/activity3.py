students = {
    "Anita": {"maths": 95, "science": 89},
    "Ravi": {"maths": 80, "science": 92},
    "Pavi": {"maths": 88, "science": 85}}

name = input("Enter student name: ")
subject = input("Enter subject name: ")
print(students.get(name, {}).get(subject, "Invalid input"))


#sol2
student={"amit":{"math":95, "science":89},
          "ravi":{"math":80, "science":92},}
print(student["ravi"]["science"])