# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# initialize even count to 0 before the loop
even_count = 0
# loop from 1 to 10
for i in range(10):
# ask the user to enter a number 10 times (since the range is 10)
# convert the input to a float
    num = float(input(f"Enter a number ({i+1}): "))
# check if the number is divisible by 2
    if num % 2 == 0:
# if it is divisible, add 1 to odd count
        even_count += 1
# print the odd count