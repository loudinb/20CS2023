import time

class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result

@Cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def time_execution(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"Execution time: {end - start:.5f} seconds")
    return result

# First execution (calculates and caches results)
print("First execution (n=30):")
result = time_execution(fibonacci, 200)
print(f"Result: {result}")

# Second execution (uses cached results)
print("\nSecond execution (n=30):")
result = time_execution(fibonacci, 200)
print(f"Result: {result}")
