from collections import namedtuple
students = namedtuple('student',['name','age','grade','marks'])
student = students("anitha",16,"A",96)
print(student.grade)