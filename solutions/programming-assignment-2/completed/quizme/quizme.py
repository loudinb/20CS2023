import random

import argparse

from data.sample_questions import QUESTIONS
from ars.arcontroller import ARController

random.shuffle(QUESTIONS)


def main():
    quiz = ARController(QUESTIONS)
    quiz.start()

if __name__ == "__main__":
