import argparse

from utils.readFile import readFile

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Input file for the program")
    args = parser.parse_args()
    input_file = args.input_file
    readFile(input_file)
