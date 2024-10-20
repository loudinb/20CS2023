# Assignment 2: QuizMe 

In this assignment, you will create a Command Line Interface (CLI) application called **QuizMe**. This application will quiz users on a set of questions, adapting to their performance using a hybrid [Leitner system](https://en.wikipedia.org/wiki/Leitner_system). The application includes an internal library called the Adaptive Review System (ARS), which provides the logic for managing the adaptive learning process.

## QuizMe CLI Application

QuizMe is the main interface through which users interact with the quiz system. You will implement a command-line interface that:

1. Loads quiz questions from a JSON data file
2. Initiates a quiz session
3. Presents questions to the user
4. Accepts and processes user answers
5. Displays feedback
6. Adapts the question order based on user performance

## Adaptive Review System (ARS) Library

The ARS is an internal library that implements the core functionality of the adaptive learning process. It uses a hybrid spaced repetition system designed for effective single-session review, combined with interval-based repetition to enhance retention.

### How ARS Works

The system uses five boxes to manage questions:

1. **Box 0 (Missed Questions)**: Prioritized for review after 60 seconds.
2. **Box 1 (Unasked Questions)**: New questions are drawn from here.
3. **Box 2 (Correctly Answered Once)**: Reviewed after 180 seconds.
4. **Box 3 (Correctly Answered Twice)**: Reviewed after 360 seconds.
5. **Box 4 (Known Questions)**: Reviewed only if all other boxes are empty.

Questions move between boxes based on the user's answers, ensuring focused attention on questions the user finds challenging while spacing out reviews for well-learned content.

## Project Structure

The project is structured into the following directories and files. The GitHub repository includes the initial setup and template files for each component, along with comprehensive test files that will be used to evaluate your implementation.

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
└── quizme.py                     # Main CLI application
```

## Assignment Tasks

Your task is to implement the following components in the specified order. Since each task builds on the previous one, it is essential to complete them sequentially and verify that each component functions correctly using the provided tests before moving on to the next.

1. Implement the [`Question` abstract base class](question-abstract-base-class.md) in `question.py`:
2. Implement the [`TrueFalse` class](truefalse-class.md) in `truefalse.py`:
3. Implement the [`ShortAnswer` class](shortanswer-class.md) in `shortanswer.py`:
4. Implement the [`Box` class](box-class.md) in `box.py`:
5. Implement the [`BoxManager` class](boxmanager-class.md) in `boxmanager.py`:
6. Implement the [`ARController` class](arcontroller-class.md) in `arcontroller.py`:
7. Implement the QuizMe CLI in `quizme.py`:
