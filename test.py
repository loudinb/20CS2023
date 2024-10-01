def test_function_1(value):
    try:
        if value == 0:
            raise ValueError("An error occurred!")
        return "From try block"
    except ValueError:
        return "From except block"
    else:
        return "From else block"
    finally:
        return "From finally block"


def test_function_2(value):
    try:
        if value == 0:
            raise ValueError("An error occurred!")
        return "From try block"
    except ValueError:
        return "From except block"
    else:
        return "From else block"
    finally:
        pass

def test_function_3(value):
    try:
        if value == 0:
            raise ValueError("An error occurred!")
    except ValueError:
        return "From except block"
    else:
        return "From else block"
    finally:
        pass
    

# Test different inputs:
print(test_function_1(1))  # Test with value = 1
print(test_function_1(0))  # Test with value = 0

print(test_function_2(1))  # Test with value = 1
print(test_function_2(0))  # Test with value = 0

print(test_function_3(1))  # Test with value = 1
print(test_function_3(0))  # Test with value = 0