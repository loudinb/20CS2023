from ars.arcontroller import ARController

# Sample question data
question_data = [
    {
        "type": "shortanswer",
        "question": "What's the capital of France?",
        "correct_answer": "Paris"
    },
    {
        "type": "truefalse",
        "question": "The Earth is flat.",
        "correct_answer": False,
        "explanation": "The Earth is actually approximately spherical."
    }
]

# Create and start the Adaptive Review Controller
controller = ARController(question_data)
controller.start()