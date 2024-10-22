import argparse
import json
from typing import Dict

def read_json_file(input_file: str) -> Dict:
    """Reads the content of a JSON file and parses it into a dictionary.

    Args:
        input_file: Path to the JSON file to be read.

    Returns:
        A dictionary representation of the JSON data.  

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDDecodeError: If the file is not valid JSON
    """
    # TODO-1: Implement try/except blocl
    # TODO-2: try block - read contents of file using json.load()
    # TODO-3: handle "FileNotFoundError" execption, return an empty dictionary
    # TODO-4: handle "json.JSONDDecodeError" exception, reutrn an empty dictionary
    pass


def process_json_file(input_file: str) -> None:
    """Reads and processes a JSON file to store its content as a dictionary.

    Args:
        input_file: Path to the JSON file.
    """
    # TODO-1: Call read_json_file to get the JSON data, json_data = ...
    # TODO-2: If json_data is not empty, print the dictionary
    pass


if __name__ == '__main__':
    # TODO-1: Create an argument parser with a description of the program
    # TODO-2: Add an argument for input_file
    
    # TODO-3: Parse the arguments
    
    # TODO-4: Call process_json_file with the input file path
    pass