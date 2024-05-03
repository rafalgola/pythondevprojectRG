import requests
from random import randint
import json

with open('..\detailedpesels.csv', 'r') as file:
    line_count = sum(1 for line in file)
    file.seek(0)
    line_number = randint(2, line_count)
    for _ in range(line_number):
        row = file.readline()
    peseltovalidate = row[0:11]
    # print(peseltovalidate)
response = requests.get(f'https://peselvalidatorapitest.azurewebsites.net/api/Pesel?pesel={peseltovalidate}')

json_response = json.loads(response.text)
# print(json_response)
print("Final operation - assertion for randomly chosen PESEl from .csv file and reply from validator.")
try:
    assert json_response['isValid'] == int(row[-2])
except AssertionError:
    print("Looks like online generator and my local validator disagreed... Shouldn't occur ;)")
else:
    print("Looks like they both have agreed - so we succeed.")
finally:
    print("Will now be quitting....")

