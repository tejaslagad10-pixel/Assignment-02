# Program to check if a number is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
print(f"{num} is an odd number.")

''

#Program to find the sum of integers from 1 to 50
total = 0
for number in range(1, 51):
    total += number
    print(f"The sum of numbers from 1 to 50 is: {total}")