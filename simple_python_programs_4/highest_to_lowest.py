# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# initialize variable to store user input, (empty list)
list_nums = []
# create infinite loop to continuously ask user to input numbers
while  True:
    try:
        num = float(input("Enter a number: "))
# add the entered number to the list
        list_nums.append(num)
# if user entered an invalid input, stop the program
    except ValueError:
        print("Sorting the numbers.....")
        break
# sort the entered numbers from highest to  lowest using sort(reverse) function
list_nums.sort(reverse=True)
# display the numbers from highest to  lowest
print("Sorted Numbers (highest to lowest): ", list_nums)