import requests
import argparse
from os.path import exists


parser = argparse.ArgumentParser(description='Gets the Advent of Code input for the given day\'s problem.')
parser.add_argument('query_date', metavar='d', type=str, help='Format: YYYY-DD')
args = parser.parse_args()

with open('creds.txt') as f:
    my_session = f.readline()

year, day = tuple(args.query_date.split('-'))

file_location = f'./{year}/day{day}/input.txt'

if not (file_exists := exists(file_location)):
    print("Input not found, attempting to retrieve input.")
    target_url = f'https://adventofcode.com/{year}/day/{day}/input'
    print(target_url)
    r = requests.get(target_url, cookies={'session': my_session})
    match r.status_code:
        case 200:
            with open(file_location, 'w') as f:
                f.write(r.text)
            print(f'Retrieval succeeded.')
        case _ as status_code:
            print(f'Retrieval failed: Status Code:{status_code}')
else:
    print(f'Input found, go here: {file_location}')
