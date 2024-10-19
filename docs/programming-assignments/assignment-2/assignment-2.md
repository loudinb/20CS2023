# Assignment 2

This assignment involves creating **QuizMe**, a Command Line Interface (CLI) application for adaptive review of study questions. QuizMe utilizes an internal library called the Adaptive Review System (ARS) which provides an efficient learning experience by adapting to the user's performance.

## QuizMe CLI Application

QuizMe is the main interface through which users interact with the quiz system. It provides a command-line interface for:

1. Loading quiz questions from a data file
2. Initiating a quiz session
3. Presenting questions to the user
4. Accepting and processing user answers
5. Displaying feedback and progress

The CLI application is responsible for the user interaction flow and integrates with the underlying ARS library to manage the adaptive review process.

## Adaptive Review System (ARS) Library

The ARS is an internal library that implements the core functionality of the adaptive review process. It uses a hybrid spaced repetition system designed for effective single-session review. The ARS combines principles of adaptive learning and interval-based repetition to enhance retention by dynamically adjusting review priorities based on performance.

### Key Components of ARS:

1. **ARController**: Manages the overall flow of the quiz session.
2. **BoxManager**: Handles the organization of questions into different "boxes" based on the user's performance.
3. **Box**: Represents a category of questions (e.g., missed, unasked, correctly answered once).
5. **Question**: Defines different types of questions (e.g., true/false, short answer).

### How ARS Works

The system uses five boxes to manage questions:

1. **Box 0 (Missed Questions)**: Prioritized for immediate review after 60 seconds.
2. **Box 1 (Unasked Questions)**: New questions are drawn from here.
3. **Box 2 (Correctly Answered Once)**: Reviewed after 360 seconds.
4. **Box 3 (Correctly Answered Twice)**: Reviewed after 600 seconds.
5. **Box 4 (Known Questions)**: Reviewed only if all other boxes are empty.

Questions move between boxes based on the user's answers and time intervals, ensuring focused attention on difficult questions while spacing out reviews for well-learned content.

## Project Structure

```
quizme/
├── ars/                          # Adaptive Review System library
│   ├── arcontroller.py
│   ├── box.py
│   ├── boxmanager.py
│   └── qtype/
│       ├── question.py
│       ├── truefalse.py
│       └── shortanswer.py
├── tests/                        # Test files for both QuizMe and ARS
│   ├── test_adaptivereview.py
│   ├── test_boxes.py
│   ├── test_card.py
│   ├── test_quizme.py
│   └── test_config.py
├── data/                         # Sample question data
│   └── example_questions.py
└── quizme.py                     # Main CLI application
```

## Assignment Tasks

1. Implement the QuizMe CLI application (`quizme.py`) that interfaces with the ARS library.
2. Complete the implementation of the ARS library components in the `ars/` directory.
3. Ensure proper integration between the CLI and the ARS library.
4. Implement loading of questions from the data file.
5. Create a user-friendly CLI experience for taking quizzes.
6. Write comprehensive tests for both the CLI application and the ARS library.

This assignment challenges you to create an effective and efficient learning tool that adapts to the user's performance in real-time, while also focusing on building a clear separation between the user interface (QuizMe CLI) and the core functionality (ARS library).