from syntax_error import Person


print("hello")

try:
    b = Person("brian")
except Exception as e:
    print(f"error: {e.__class__.__name__} {e}")

print("goodye")
