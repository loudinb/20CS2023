import random
from data.sample_questions import QUESTIONS
from ars.arcontroller import ARController

random.shuffle(QUESTIONS)
quiz = ARController(QUESTIONS)
quiz.start()