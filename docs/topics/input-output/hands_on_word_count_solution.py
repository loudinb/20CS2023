import argparse
from typing import Dict, List
import re
from collections import Counter

def read_text_file(input_file: str) -> str:
    """Reads the content of a text file.

    Args:
        input_file: Path to the text file to be read.

    Returns:
        The content of the file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open(input_file, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        raise


def clean_and_split_text(text: str) -> List[str]:
    """Cleans and splits the text into words.

    Args:
        text: The raw text data.

    Returns:
        A list of words after converting to lowercase and removing punctuation.
    """
    # Convert text to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split the text into words
    return text.split()


def count_words(words: List[str]) -> Dict[str, int]:
    """Counts the occurrences of each word in a list.

    Args:
        words: A list of words.

    Returns:
        A dictionary where keys are words and values are their counts.
    """
    return dict(Counter(words))


def display_word_counts(word_counts: Dict[str, int]) -> None:
    """Displays the word counts.

    Args:
        word_counts: A dictionary of word counts.
    """
    # Sort the words alphabetically and display counts
    for word in sorted(word_counts):
        print(f"{word}: {word_counts[word]}")


def process_text_file(input_file: str) -> None:
    """Processes a text file to count word occurrences and display the results.

    Args:
        input_file: Path to the input text file.
    """
    try:
        content = read_text_file(input_file)
        if not content.strip():
            print("Warning: The file is empty.")
            return
        words = clean_and_split_text(content)
        word_counts = count_words(words)
        display_word_counts(word_counts)
    except Exception as e:
        print(f"An error occurred during processing: {e}")


if __name__ == '__main__':
    # Create a parser with a description of the program
    parser = argparse.ArgumentParser(description="Count word occurrences in a text file.")

    # Add an argument for input_file
    parser.add_argument("--input_file", required=True, help="Path to the input text file")

    # Parse the arguments
    args = parser.parse_args()

    # Process the text file
    process_text_file(args.input_file)
