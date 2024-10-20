"""
QuizMe: An adaptive quiz Command Line Interface (CLI) application.

This script allows users to take an adaptive quiz based on questions loaded from a JSON file.
It uses the Adaptive Review System (ARS) to manage the quiz session.
"""

import json
import argparse
from pathlib import Path
from typing import List, Dict, Any

from ars.arcontroller import ARController

def load_questions(file_path: Path) -> List[Dict[str, Any]]:
    """
    Load questions from a JSON file.

    Args:
        file_path (Path): Path to the JSON file containing quiz questions.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, each representing a quiz question.

    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with file_path.open('r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Question file not found at {file_path}")
        raise
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in question file {file_path}")
        raise

def run_quiz(name: str, questions: List[Dict[str, Any]]) -> None:
    """
    Run the adaptive quiz session.

    Args:
        name (str): The name of the quiz taker.
        questions (List[Dict[str, Any]]): A list of dictionaries containing question data.
    """
    print(f"Welcome, {name}! Let's start your adaptive quiz session.")
    quiz = ARController(questions)
    quiz.start()

def main() -> None:
    """
    Main function to set up and run the QuizMe CLI application.
    """
    parser = argparse.ArgumentParser(description="QuizMe: An adaptive quiz application")
    parser.add_argument("name", type=str, help="Your name")
    parser.add_argument("--questions", type=str, required=True, help="Path to the question data file")

    args = parser.parse_args()

    questions_path = Path(args.questions)
    try:
        questions = load_questions(questions_path)
        run_quiz(args.name, questions)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Exiting due to error in loading questions.")

if __name__ == "__main__":
    main()
