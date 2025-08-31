
n = int(input("Enter a positive integer: "))

total = 0   
num = 1     

while num <= n:
    total += num
    num += 1

print(f"The sum of all natural numbers from 1 to {n} is {total}")
