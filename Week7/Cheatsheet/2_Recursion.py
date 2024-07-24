# Put simply, recursion is the process of a function calling itself.
#
# Example Usage:


def recursive_crash():
    print("I will run forever")
    recursive_crash()

# If we call the function recursive_crash() above, it will
# print "I will run forever" and then call itself, causing the function
# to execute again. "I will run forever" will repeat again, and the function
# will call itself again. This will happen over and over until your program crashes.

i = 0
while i < 10:
    recursive_crash()
    i += 1