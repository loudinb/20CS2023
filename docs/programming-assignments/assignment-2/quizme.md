# `quizme` CLI

The `quizme.py` file serves as the main Command Line Interface (CLI) for the QuizMe application. It handles user interaction, loads quiz questions, and manages the quiz session using the Adaptive Review System (ARS).

Follow the specifications provided below to implement the `quizme.py` file. The module-level docstring should be:

```python
"""
QuizMe: An adaptive quiz Command Line Interface (CLI) application.

This script allows users to take an adaptive quiz based on questions loaded from a JSON file.
It uses the Adaptive Review System (ARS) to manage the quiz session.
"""
```

## Functions

| Name            | Parameters                              | Return Type | Description                                   |
|-----------------|---------------------------------------- |-------------|-----------------------------------------------|
| load_questions  | file_path: Path                         | List[Dict[str, Any]] | Load questions from a JSON file       |
| run_quiz        | name: str, questions: List[Dict[str, Any]] | None     | Run the adaptive quiz session                 |
| main            | None                                    | None        | Main function to set up and run the QuizMe CLI|

### Implementation Details

**`load_questions(file_path: Path) -> List[Dict[str, Any]]`**
- Implement this function to load questions from a JSON file.
- Add a docstring to describe the function:
  ```python
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
  ```
- Use a try-except block to handle potential `FileNotFoundError` and `json.JSONDecodeError`.
- If an error occurs, print an appropriate error message and re-raise the exception.

**`run_quiz(name: str, questions: List[Dict[str, Any]]) -> None`**
- Implement this function to run the adaptive quiz session.
- Add a docstring to describe the function:
  ```python
  """
  Run the adaptive quiz session.

  Args:
      name (str): The name of the quiz taker.
      questions (List[Dict[str, Any]]): A list of dictionaries containing question data.
  """
  ```
- Print a welcome message including the user's name.
- Create an instance of `ARController` with the loaded questions.
- Call the `start` method of the `ARController` instance to begin the quiz session.

**`main() -> None`**
- Implement this function as the entry point for the QuizMe CLI application.
- Add a docstring to describe the function:
  ```python
  """
  Main function to set up and run the QuizMe CLI application.
  """
  ```
- Set up an `argparse.ArgumentParser` to handle command-line arguments:
  - Add a positional argument `name` for the user's name.
  - Add a required argument `--questions` for the path to the question data file.
- Parse the command-line arguments.
- Use a try-except block to:
  - Load questions using the `load_questions` function.
  - Run the quiz using the `run_quiz` function.
- Handle potential exceptions from `load_questions` and print an error message if they occur.

## Script Execution

At the end of the file, include the following code to ensure the script can be run directly:

```python
if __name__ == "__main__":
    main()
```

### Testing the QuizMe CLI

To test the QuizMe CLI, you can run it from the command line with a sample JSON file containing quiz questions. Here's an example of how to use the CLI:

```bash
python quizme.py John --questions sample_questions.json
```