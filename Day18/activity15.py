def div():
    numerator = int(input("Enter numerator: "))
    while True:
        denominator = int(input("Enter denominator: "))
        try:
            result = numerator / denominator
            print("Result:", result)
            break
        except ZeroDivisionError:
            print("Cannot divide by zero!")
div()
