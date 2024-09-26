class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
    
    def __call__(self, *args):
        if args in self.cache:
            print(f"Using cached result for {args}")
            return self.cache[args]
        print(f"Calculating for {args}")
        result = self.func(*args)
        self.cache[args] = result
        return result

@Memoize
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
