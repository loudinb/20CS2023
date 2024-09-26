import time

class Timer:
    def __init__(self, func):
        # TODO: Create instance variables to store the function
        pass

    def __call__(self, *args):
        # TODO: Assign the start time to a variable
        # TODO: Call the original function
        # TODO: Assign the end time to a variable
        # TODO: Calculate the elapsed time
        # TODO: Print the elapsed time to the screen
        # TODO: Return the result of the original function

        pass

    
# Example function to be timed
@Timer
def sum_of_n(n):
    return sum(range(1, n + 1))

result = sum_of_n(1000000)
print(result)
