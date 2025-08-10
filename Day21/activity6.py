employee = "Abi"
hours_worked = 45.75
hourly_rate = 350.50
bonus = 1500
target_hours = 40
print(f"{'Employee Report':*^40}\n")
print(f"Employee Name: {employee:>20}")
print(f"Hours Worked : {hours_worked:>20}")
print(f"Target Hours : {target_hours:>20}")
print(f"Overtime     : {(hours_worked-target_hours):>20.2f}")
print(f"Total Pay    : ${((target_hours*hourly_rate)+((hours_worked-target_hours)*hourly_rate)+bonus):010.2f}")

