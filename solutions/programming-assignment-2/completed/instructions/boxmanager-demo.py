from ars.qtype.shortanswer import ShortAnswer
from ars.boxmanager import BoxManager

# Create a BoxManager
box_manager = BoxManager()

# Create some questions
q1 = ShortAnswer("What's the capital of France?", "Paris")

# Add questions to the BoxManager
box_manager.add_new_question(q1)

# Get the next question
next_question = box_manager.get_next_question()
if next_question:
    print(next_question.ask())
    user_answer = input("Your answer: ")
    correct = next_question.check_answer(user_answer)
    if correct:
        print("Correct!")
    else:
        print(next_question.incorrect_feedback())
    box_manager.move_question(next_question, correct)