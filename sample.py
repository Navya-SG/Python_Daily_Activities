# # def custom_sum(numbers):
# #     total = 0
# #     for num in numbers:
# #         total += num
# #     return total
# # print(custom_sum([10,40,30,50]))

# # def greet():
# #     """navya function"""
# #     return("navya")
# # print(greet.__doc__)

# ''
# 'modules'
# 'analyze'
# 'process datqa to zip file'
# 'send'

# students = [
#     {"name": "Alice", "scores": [95, 92, 88]},
#     {"name": "Bob", "scores": [70, 85, 78]},
#     {"name": "Charlie", "scores": [100, 98, 95]},
#     {"name": "David", "scores": [90, 90, 90]}
# ]

# # Dictionary comprehension to filter students with average >= 90
# high_achievers = {
#     student["name"]: sum(student["scores"]) / len(student["scores"])
#     for student in students
#     if sum(student["scores"]) / len(student["scores"]) >= 90
# }

# print(high_achievers)


# students = [{"name": "Brenda", "scores": [90, 92, 95, 88]},
#             {"name": "David", "scores": [85, 87, 89]},
#             {"name": "Cathy", "scores": [98, 99, 100]},
#             {"name": "Alex", "scores": [70, 100]}]
# for i in students:
#         avg=(sum(students["scores"])/len(students["scores"]))
#         if avg >= 90:
#             print(students["name"])


with open("giphy.jpg","rb") as file:
    data = file.read()
    print(data)