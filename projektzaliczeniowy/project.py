import datacollection
import assertion
import os

chromedriver_path = r'.\projektzaliczeniowy\chromedriver.exe'


def chromedriver_in_path():
    paths = os.environ['PATH'].split(os.pathsep)
    for path in paths:
        if os.path.exists(os.path.join(path, 'chromedriver.exe')):
            return True
    return False


if os.path.exists(chromedriver_path) or chromedriver_in_path():
    datacollection.check_files()
    datacollection.collect_detailed_data_from_online_generator()
    assertion.arrange_assert()
else:
    print("Download chromedriver.exe in 'projektzaliczeniowy' directory ( or into $PATH ) and then run main.py again.")
