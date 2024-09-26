import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        start_time = time.time()  # Record the start time
        result = self.func(*args)  # Call the original function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time
        
        # Log the execution time to the screen
        print(f"Function executed in {elapsed_time:.4f} seconds")
        
        return result

# Example function to be timed
@Timer
def sum_of_n(n):
    return sum(range(1, n + 1))
