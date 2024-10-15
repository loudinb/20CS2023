import argparse

parser = argparse.ArgumentParser()

# Store a single value
parser.add_argument('--name', action='store', help='Your name')

# Store a constant value
parser.add_argument('--verbose', action='store_const', const=True, help='Enable verbose mode')

# Store True when argument is present
parser.add_argument('--debug', action='store_true', help='Enable debug mode')

# Count occurrences
parser.add_argument('-v', '--verbose2', action='count', help='Increase verbosity')

# Append values to a list
parser.add_argument('--file', action='append', help='List of files')

args = parser.parse_args()

print(args)
