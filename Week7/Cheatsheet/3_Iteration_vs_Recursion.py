# Iteration vs Recursion
# Like a for loop or while loop (also referred to as
# iteration), recursion is a way to repeatedly
# execute a chunk of code. In fact, recursion and
# iteration both achieve the same goal
# (repetition), but with inverse approaches.
#
# Iteration uses a bottom-up approach. It begins
# by solving the smallest subproblem and then
# works it way up to solving larger and larger
# subproblems, working our way up to a solution
# to the overall problem.
#
# In contrast, recursion uses a top-down
# approach. It takes the overall problem and
# breaks it apart into smaller and smaller
# subproblems until it finally finds one that can be
# solved readily. Then, if necessary, recursion
# follows the same pattern as iteration of using
# the subproblem solutions to build back up to
# the overall solution.

#Iterative Approach
def count_iterative(num):
    i = 1
    while i <= num:
        print(f"Count {i}!")
        i += 1

# Input: 5
# Output:
# "Count 1!"
# "Count 2!"
# "Count 3!"
# "Count 4!"
# "Count 5!"

#Recursive Approach
def count_recursive(num):
    print(f"Count {num}!")
    if num == 1:
        return
    else:
        count_recursive(num - 1)

# Input: 5
# Output:
# "Count 5!"
# "Count 4!"
# "Count 3!"
# "Count 2!"
# "Count 1!"

# In the example above, the iterative approach
# uses a loop to repeat code. A loop variable i is
# initialized, and Count {i} is printed once. and
# then the function works forward, repeating the
# loop body. We move towards ending the
# repetition by incrementing i to a larger or larger
# value until the overall goal is achieved (printing
# Count {i} i number of times).
#
# In contrast, the recursive function starts by
# printing the input value, num, then creates
# repetition by calling itself so that the function
# body repeats. It moves towards terminating the
# repetition by decrementing the argument num
# with each new function call, finally terminating
# the cycle of function calls with a return
# statement when we reach the smallest possible
# value for num, 1.
#
