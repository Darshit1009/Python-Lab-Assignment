
num = int(input("Enter a number: "))
num = abs(num)


if num == 0:
    product = 0
else:
    product = 1
    while num > 0:
        digit = num % 10       
        product *= digit       
        num //= 10            

print(f"The product of digits is {product}")
