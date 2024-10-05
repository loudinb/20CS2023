import random

correct_answers = 0

while correct_answers < 10:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2

    user_input = input(f"What is {num1} x {num2}? ")
    if user_input.lower() == "exit":
        break

    try:
        user_answer = int(user_input)
    except ValueError:
        print("Please enter a valid integer or 'exit' to quit.")
        continue
    
    if user_answer == answer:
        print("Correct!")
        correct_answers += 1
    else:
        print(f"Incorrect! The correct answer is {answer}.")


if correct_answers == 10:
    print("Congratulations! You've answered 10 questions correctly.")
else:
    print("Remember, practice makes perfect! Goodbye!")