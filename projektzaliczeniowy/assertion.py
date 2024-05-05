import requests
from random import randint
import json
from datetime import datetime


def arrangassert():
    """This function makes an assertion - if no AssertionError returned means my api with validator works fine."""
    with open('detailedpesels.csv', 'r') as file:
        line_count = sum(1 for line in file)
        file.seek(0)
        line_number = randint(2, line_count)
        for _ in range(line_number):
            row = file.readline()
        peseltovalidate = row[0:11]
    response = requests.get(f'http://127.0.0.1:8000/Pesel?pesel={peseltovalidate}')

    json_response = json.loads(response.text)
    # print(json_response)
    print(f'Final operation - assertion for randomly chosen from .csv file {peseltovalidate} and reply from validator:')
    try:
        assert json_response['result'] == int(row[-2])
    except AssertionError:
        print("Looks like online generator and my local validator disagreed... Shouldn't occur ;)")
    else:
        print("No assertion error  - so project SUCCEEDED :)")
        with open('assertions.log', 'a') as file:
            file.write(f'{datetime.now()} - Test for {peseltovalidate} PASSED.\n')
    finally:
        print("Will now start quitting....")
    return None
