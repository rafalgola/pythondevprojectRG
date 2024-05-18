import requests
from random import randint
import json
from datetime import datetime
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projektzaliczeniowy.settings')
django.setup()


def arrange_assert():
    """This function makes an assertion - if no AssertionError returned means my api with validator works fine."""
    from walidator import models
    with open('detailedpesels.csv', 'r') as file:
        line_count = sum(1 for line in file)
        file.seek(0)
        line_number = randint(2, line_count)
        for _ in range(line_number):
            row = file.readline()
        peseltovalidate = row[0:11]
    response = requests.get(f'http://127.0.0.1:8000/Pesel?pesel={peseltovalidate}')

    json_response = json.loads(response.text)
    print(f'Final operation - assertion for randomly chosen from .csv file {peseltovalidate} and reply from validator:')

    try:
        assert json_response['result'] == int(row[-2])
    except AssertionError:
        print("Looks like online generator and my local validator disagreed... Shouldn't occur ;)")
        write_to_db = models.Asserted_Pesels(stamp=str(datetime.now())[:16],
                                             pesel=peseltovalidate,
                                             assertion_result='False')
        write_to_db.save()
        pass
    else:
        print("No assertion error  - so project SUCCEEDED :)")
        write_to_db = models.Asserted_Pesels(stamp=str(datetime.now())[:16],
                                             pesel=peseltovalidate,
                                             assertion_result='True')
        write_to_db.save()
        # with open('assertions.log', 'a') as file:
        #     file.write(f'{datetime.now()} - Test for {peseltovalidate} PASSED.\n')
    finally:
        print("Will now start quitting....")
