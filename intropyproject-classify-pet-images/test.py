import argparse

# Create ArgumentParser object
parser = argparse.ArgumentParser(description='Description of your program')

# Add arguments
parser.add_argument('filename', help='Name of the file to process')
parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose mode')

# Parse the arguments
args = parser.parse_args()

# Access parsed arguments
filename = args.filename
verbose = args.verbose

# Use the arguments
print("Filename:", filename)
if verbose:
    print("Verbose mode is enabled")
