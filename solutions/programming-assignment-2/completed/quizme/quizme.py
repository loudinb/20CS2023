import random
import json
import argparse
from ars.arcontroller import ARController
from pathlib import Path

# Get the current directory


def main(name, questions_path):
    
    current_dir = Path.cwd()
    questions_path = current_dir / questions_path
    
    # Opening JSON file
    f = open(questions_path)
    questions = json.load(f)
    f.close()

    random.shuffle(questions)

    quiz = ARController(questions)
    quiz.start()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="QuizMe: An adaptive quiz application")
    parser.add_argument("name", type=str, help="Enter your name")
    parser.add_argument("--questions", type=str, required=True, help="Path to the question data file")

    args = parser.parse_args()
    print(args.questions)
    main(args.name, args.questions)



