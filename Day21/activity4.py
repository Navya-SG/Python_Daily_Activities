'''The % operator,tells Python - Take the format string on the left, and fill in the placeholders using the values from the tuple on the right'''

employees = [
    ("Alice", 28, 52345.75),
    ("Bob", 35, 62300.5),
    ("Charlie", 41, 70000.0),
    ("Dana", 25, 48750.2),]
print("%-10s %-4s %011s" % ("Name","Age","Salary"))
for name,age,salary in employees:
    print("%-10s %-4d %011.2f" % (name,age,salary))

