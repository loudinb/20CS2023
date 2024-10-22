import argparse
import json
from typing import Dict

def read_json_file(input_file: str) -> Dict:
    """Reads the content of a JSON file and parses it into a dictionary.

    Args:
        input_file: Path to the JSON file to be read.

    Returns:
        A dictionary representation of the JSON data.
    """
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{input_file}' is not a valid JSON file.")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}


def process_json_file(input_file: str) -> None:
    """Reads and processes a JSON file to store its content as a dictionary.

    Args:
        input_file: Path to the JSON file.
    """
    json_data = read_json_file(input_file)
    if json_data:
        print(json_data)


if __name__ == '__main__':
    # Create an argument parser with a description of the program
    parser = argparse.ArgumentParser(description="Read a JSON file and display its contents.")
    
    # Add an argument for the input file
    parser.add_argument('input_file', type=str, help="Path to the JSON file")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Call process_json_file with the input file path
    process_json_file(args.input_file)
