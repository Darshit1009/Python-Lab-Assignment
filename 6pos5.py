num = int(input("Enter a number: "))

is_negative = num < 0
num = abs(num)

num_str = str(num)

if len(num_str) == 1:
    swapped_num = num
else:
    swapped_str = num_str[-1] + num_str[1:-1] + num_str[0]
    swapped_num = int(swapped_str)


if is_negative:
    swapped_num = -swapped_num

print(f"Number after swapping first and last digits: {swapped_num}")
