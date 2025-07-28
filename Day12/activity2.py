'''You are the at Eagle Airbase. A severe sandstorm has damaged all computer tracking systems. Multiple fighter jets were sent on patrol missions this morning, but the storm is making radio communication difficult.
MISSION DATA:
Your ground crew chief provides you with handwritten flight logs:
601, 602, 603, 608, 612, 615, 618
601, 603, 608, 612, 615, 618
YOUR TASK:
Using the aircraft numbers provided and basic mathematical operations, determine which specific aircraft has not returned to base.
SYSTEM CONSTRAINTS:
Your emergency calculator can only do basic math operations
No advanced programming features available
Cannot use lists, loops, or complex functions
Must use only simple mathematical calculations
COMMANDER'S INSTRUCTION:
  "Lieutenant, we need to know immediately which aircraft is missing. Use whatever mathematical method you can think of to process these numbers. The pilot needs emergency landing guidance - time is critical!"  
SAMPLE DATA:
601, 602, 603, 608, 612, 615, 618
601, 603, 608, 612, 615, 618
?'''

#sol 1
data1=601+602+603+608+612+615+618 
data2=601+603+608+612+615+618
print(data1-data2)


#sol 2
'''
SAMPLE DATA:
data = 103,103,105,103,103,105,107,108,108
'''
data=103,103,105,103,103,105,107,108,108
a1 = 103
a2 = 103
a3 = 105
a4 = 103
a5 = 103
a6 = 105
a7 = 107
a8 = 108
a9 = 108
total_sum = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
# Unique aircrafts: 103, 105, 107, 108
# Expected counts: 103 (4), 105 (2), 107 (2), 108 (2)
# Expected sum = 103*4 + 105*2 + 107*2 + 108*2
expected_sum = 103*4 + 105*2 + 107*2 + 108*2
missing_aircraft = expected_sum - total_sum
print(f"The missing aircraft is: {missing_aircraft}")


#final solution
print("The missing aircraft is:", 103^103^105^103^103^105^107^108^108)
