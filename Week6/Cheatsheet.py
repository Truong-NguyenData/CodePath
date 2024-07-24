# Chained Assignment
# In Python, chained assignment is a convenient shorthand
# syntax that allows us to assign multiple variables to the same
# value with a single line of code.
#
# Chained assignment can help improve readability when initializing
# or updating multiple variables to the same value.
#
# Example Usage:

x = y = z = 3
print(x) # Prints 3
print(y) # Prints 3
print(z) # Prints 3

#----------------------
# Break Statements
# The break keyword is used to break out of a loop early.
# When we add a break statement, the loop immediately terminates. Try it
#
# Example Usage:
#
# # Example 1: While Loop
count = 1
while count <= 10:
    if count == 5:
        break  # Break the loop if count reaches 5
    print(count)
    count += 1

# Example 2: For Loop
numbers = [1, 3, 5, 7, 9, 2, 4]
for number in numbers:
    if number % 2 == 0:
        print(f"First even number found: {number}")
        break


