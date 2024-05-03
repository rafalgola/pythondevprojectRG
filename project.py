# import django
import time
import datacollection
import os

chromdriver_path = r'.\chromedriver.exe'


def chromedriver_in_path():
    paths = os.environ['PATH'].split(os.pathsep)
    for path in paths:
        if os.path.exists(os.path.join(path, 'chromedriver.exe')):
            return True
    return False


if os.path.exists(chromdriver_path) or chromedriver_in_path():
    print("Jest driver")
    datacollection.check_files()
    datacollection.collect_detailed_data_from_online_generator()
else:
    print("Download chromedriver.exe in 'projektzaliczeniowy' directory ( or into $PATH ) and then run main.py again.")
print("About to finish in 10 s")
time.sleep(10)
