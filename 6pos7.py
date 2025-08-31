
num = int(input("Enter a number: "))
is_negative = num < 0
num = abs(num)

reverse_num = 0
while num > 0:
    digit = num % 10         
    reverse_num = reverse_num * 10 + digit
    num //= 10               

if is_negative:
    reverse_num = -reverse_num

print(f"The reverse of the number is: {reverse_num}")
