from ars.qtype.shortanswer import ShortAnswer

sa_question = ShortAnswer(
    question="What is the capital of France?",
    answer="Paris",
    case_sensitive=False
)

print(sa_question.ask())  # Outputs: What is the capital of France?

user_input = input("Your answer: ")
if sa_question.check_answer(user_input):
    print("Correct!")
else:
    print(sa_question.incorrect_feedback())