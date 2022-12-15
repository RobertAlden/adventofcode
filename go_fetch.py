import os
import requests
import argparse

parser = argparse.ArgumentParser(description='Gets the Advent of Code input for the given day\'s problem.')
parser.add_argument('query_date', metavar='d', type=str, help='Format: YYYY-DD')
args = parser.parse_args()

with open('creds.txt') as f:
    my_session = f.readline()

year, day = tuple(args.query_date.split('-'))

file_location = f'./{year}/day{day}/input.txt'

if not (file_exists := os.path.exists(file_location)):
    print("Input not found, attempting to retrieve input.")
    target_url = f'https://adventofcode.com/{year}/day/{day}/input'
    print(target_url)
    r = requests.get(target_url, cookies={'session': my_session})
    match r.status_code:
        case 200:
            if not os.path.exists(file_location[:-9]):
                os.makedirs(file_location[:-9])
            print(f'Retrieval succeeded.')
            if not os.path.exists(file_location[:-9] + f'day{day}.py'):
                cmd = f'copy \"{os.getcwd()}\\{year}\\_new\\rename_me.py\" \"{os.getcwd()}\\{year}\\day{day}\\day{day}.py\"'
                os.system(cmd)
            if not os.path.exists(file_location[:-9] + f'test.txt'):
                with open(file_location[:-9] + 'test.txt', 'w') as f:
                    f.write("GO FIND THE TEST INPUT LOSER")

        case _ as status_code:
            print(f'Retrieval failed: Status Code:{status_code}')
else:
    print(f'Input found, go here: {file_location}')
