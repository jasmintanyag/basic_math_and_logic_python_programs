# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# initialize variable to store user input, (empty list)
list_nums = []
# create infinite loop to continuously ask user to input numbers
while True:
    try:
        num = float(input("Enter a number: "))
# add the entered number to the list
        list_nums.append(num)
# if user entered an invalid input, stop the program
    except ValueError:
        print("Sorting the numbers.....")
        break
# sort the entered numbers from lowest to highest using sort() function
list_nums.sort()
# display the numbers from highest to lowest
print("Sorted Numbers (lowest to highest): ", list_nums)