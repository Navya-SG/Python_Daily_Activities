'''x = 10 
def outer():
    x = 20  
    def inner():
        x = 30  
        print(x)
    inner()
outer()'''

def process_numbers(numbers):
    even_numbers = []
    
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            yield f"Odd number found: {num}"
    
    return even_numbers

nums = [1, 2, 3, 4, 5, 6]
gen = process_numbers(nums)

for msg in gen:
    print(msg)

