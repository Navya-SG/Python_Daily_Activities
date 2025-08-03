
def avg(*scores):
    return (sum(scores)/len(scores))
print(avg(80,90,100))


# def custom_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# print(custom_sum([10,40,30,50]))

def greet():
    """navya function"""
    return("navya")
print(greet.__doc__)
