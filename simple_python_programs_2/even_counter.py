# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

'''
initialize even count to 0 before the loop
loop from 1 to 10
ask the user to enter a number 10 times (since the range is 10)
convert the input to a float
check if the number is divisible by 2
if it is divisible, add 1 to odd count
print the even count
'''

even_count = 0
for i in range(10):
    num = float(input(f"Enter a number ({i+1}): "))
    if num % 2 == 0:
        even_count += 1
print(f"There are {even_count} even number/s.")