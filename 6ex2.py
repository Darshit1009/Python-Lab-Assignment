def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5)) 


def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  
.
