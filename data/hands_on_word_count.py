import argparse
from typing import Dict

def read_text_file(input_file: str) -> str:
    """Reads the content of a text file.

    Args:
        input_file: Path to the text file to be read.

    Returns:
        The content of the file as a string.
    """
    # TODO: Open the input file in text read mode
    #       Read the entire file content and return it
    pass


def clean_and_split_text(text: str) -> list:
    """Cleans and splits the text into words.

    Args:
        text: The raw text data.

    Returns:
        A list of words after converting to lowercase and removing punctuation.
    """
    # TODO: Convert text to lowercase
    #       Remove punctuation (e.g., .,!?)
    #       Split the text into words and return the list
    pass


def count_word_occurrences(words: list) -> Dict[str, int]:
    """Counts the occurrences of each word in a list.

    Args:
        words: A list of words.

    Returns:
        A dictionary where keys are words and values are their counts.
    """
    # TODO: Create a dictionary to store word counts
    #       Iterate over the words and update the counts
    pass


def display_word_counts(word_counts: Dict[str, int]) -> None:
    """Displays the word counts.

    Args:
        word_counts: A dictionary of word counts.
    """
    # TODO: Print each word and its corresponding count
    #       Sort the words alphabetically for better readability
    pass


def process_text_file(input_file: str) -> None:
    """Processes a text file to count word occurrences and display the results.

    Args:
        input_file: Path to the input text file.
    """
    # TODO-1: Call read_text_file to get the file content
    # TODO-2: Call clean_and_split_text to get a list of words
    # TODO-3: Call count_word_occurrences to count the words
    # TODO-4: Call display_word_counts to show the results
    pass


if __name__ == '__main__':
    # TODO-1: Create a parser with a description of the program
    # TODO-2: Add an argument for input_file
    
    # TODO-3: Parse the arguments
    
    # TODO-4: Call process_text_file with the input file path
