try:
  number = int(input("Enter a number: "))
  result = 10 / number
  print("The result is:", result)
except ZeroDivisionError:
  print("Division by zero is not allowed.")
except ValueError:
  print("Invalid input. Please enter a valid number.")


my_list = [1, 2, 3, 4, 5]
print(len(my_list))


def add_numbers(a, b):
    return a + b
result = add_numbers(3, 5)
print(result)

