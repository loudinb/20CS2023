import random
from data.sample_questions import QUESTIONS
from ars.adaptivereview import AdaptiveReview

random.shuffle(QUESTIONS)
quiz = AdaptiveReview(QUESTIONS)
quiz.start()