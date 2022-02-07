try:
    numerator = int(input("Number to divide:"))
    denominator = int(input("Number to divide by:"))
    result = numerator / denominator
except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print("Invalid input")
except Exception as e:
    print("Something went wrong: {}".format(e))
else:
    print("Result is {}".format(result))