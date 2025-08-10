#concat str + int
name = "Alice"
age = 30
print("Name: " + name + ", Age: " + str(age))

#format %
name = "Hi"
number = 42
pi = 3.14159
large = 1500

print("%s" % name)    # %s → string
print("%r" % name)    # %r → repr string
print("%d" % number)  # %d → decimal integer
print("%i" % number)  # %i → integer
print("%f" % pi)      # %f → float (6 decimals)
print("%e" % large)   # %e → scientific notation
print("%%")           # %% → prints a literal %

#align format
print("HI","%-5d" % 42,"Hi") #HI 42    Hi    left align 5 space %5d
print("HI","%5d" % 42,"Hi")  #HI    42 Hi    right align %-5d 5 space
print("HI","%05d" % 42,"Hi") #HI 00042 Hi    right align with replace 0 "%05d"
print("%.2f" % 3.14159)      #3.14           2 decimal %.2f
print("%8.2f" % 3.14159)     #    3.14       rightalign 8 space + decimal %8.2f

#act1
employees = [
    ("Alice", 28, 52345.75),
    ("Bob", 35, 62300.5),
    ("Charlie", 41, 70000.0),
    ("Dana", 25, 48750.2)]
print("%-10s %-3s %s" % ("Name", "Age", "Salary"))
for a,b,c in employees:
    print("%-10s %-3d %d" % (a,b,c))

# .format()
print("Hello, {}".format("Alice"))
print("Hello, {}. I'm {}".format("Alice",22))
print("Hello, {name}. I'm {age}".format(name="Alice",age=22))
print("Hello, {1}. I'm {0}".format(22,"Alice"))

#"{position:fill align width}".format(value)
print("{:>5}".format("Hi"))         #'   Hi'
print("{:*>5}".format("Hi"))        #'***Hi'
print("{:<5}".format("Hi"))         #'Hi   '
print("{:.<5}".format("Hi"))        #'Hi...'
print("{:^7}".format("Hi"))         #'  Hi   '
print("{:_^7}".format("Hi"))        #'__Hi___'
print("{0:>6}".format("Navya","hi"))#' Navya'
print("{1:>6}".format("Navya","hi"))#'    hi'

#f"{}"
name="Navya"
age = 20
print(f"{age=}") #age=20
print(f"{name.upper()} is {age} years old.") #NAVYA is 20 years old.
print(f"In 5 years, {name} will be {age + 5}") #In 5 years, Navya will be 25
print(f"{3.14159:>8.2f}") #'    3.14'

#act2
name='Tanvi'
subject="Mathematics"
marks = 94.756
grade = "A"
print("{0:<10} | Subject:{1} | Marks:{2:>9.2f} | Grade:{3:>2}".format(name,subject,marks,grade))
#Tanvi    | Subject: Mathematics | Marks:   94.76 | Grade: A

#act3
employee = "Abi"
hours_worked = 45.75
hourly_rate = 350.50
bonus = 1500
target_hours = 40
print(f"{'Employee Report':*^40}")
print(f"{'Employee Name:':>20} {employee:>20}")
print(f"{'Hours worked:':>20} {hours_worked:>20}")
print(f"{'Target Hours:':>20} {target_hours:>20}")
print(f"{'Overtime:':>20} {hours_worked-target_hours:>20}")
print(f"{'Total Pay':>19}: ${(hours_worked*hourly_rate+bonus):010.2f}")
 