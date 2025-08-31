def count_digits(num):
 
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count



number = int(input("Enter a number: "))
print(f"Number of digits in {number} is {count_digits(number)}")
