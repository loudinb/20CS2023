import argparse
from typing import Dict
import re

def read_text_file(input_file: str) -> str:
    """Reads the content of a text file.

    Args:
        input_file: Path to the text file to be read.

    Returns:
        The content of the file as a string.
    """
    with open(input_file, "r") as file:
        content = file.read()
    return content


def clean_and_split_text(text: str) -> list:
    """Cleans and splits the text into words.

    Args:
        text: The raw text data.

    Returns:
        A list of words after converting to lowercase and removing punctuation.
    """
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Split the text into words
    words = text.split()
    return words


def count_word_occurrences(words: list) -> Dict[str, int]:
    """Counts the occurrences of each word in a list.

    Args:
        words: A list of words.

    Returns:
        A dictionary where keys are words and values are their counts.
    """
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def display_word_counts(word_counts: Dict[str, int]) -> None:
    """Displays the word counts.

    Args:
        word_counts: A dictionary of word counts.
    """
    # Sort the words alphabetically
    for word in sorted(word_counts):
        print(f"{word}: {word_counts[word]}")


def process_text_file(input_file: str) -> None:
    """Processes a text file to count word occurrences and display the results.

    Args:
        input_file: Path to the input text file.
    """
    # Step 1: Read the file content
    content = read_text_file(input_file)

    # Step 2: Clean and split the text into words
    words = clean_and_split_text(content)

    # Step 3: Count the word occurrences
    word_counts = count_word_occurrences(words)

    # Step 4: Display the word counts
    display_word_counts(word_counts)


if __name__ == '__main__':
    # Create a parser with a description of the program
    parser = argparse.ArgumentParser(description="Count word occurrences in a text file.")

    # Add an argument for input_file
    parser.add_argument("--input_file", required=True, help="Path to the input text file")

    # Parse the arguments
    args = parser.parse_args()

    # Call process_text_file with the input file path
    process_text_file(args.input_file)
