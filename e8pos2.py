import math

def calculate_y(x):
    return 6 * x ** 2 + 4 * math.sin(x)
from e8pos2 import calculate_y

x = int(input("Enter the value :"))
result = calculate_y(x)
print(result)
