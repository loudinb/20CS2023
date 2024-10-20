from ars.qtype.truefalse import TrueFalse

tf_question = TrueFalse(
    question="Python is a statically typed language.",
    answer=False,
    explanation="Python is actually a dynamically typed language."
)

print(tf_question.ask())  # Outputs: Python is a statically typed language. (True/False)

user_input = input("Your answer (True/False): ")
if tf_question.check_answer(user_input):
    print("Correct!")
else:
    print(tf_question.incorrect_feedback())