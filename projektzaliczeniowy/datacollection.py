from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import datetime
import string_utils
from faker import Faker


def check_files():
    try:
        with open('detailedpesels.csv', 'r') as file:
            print('Found detailedpesels.csv')
    except FileNotFoundError:
        with open('detailedpesels.csv', 'a') as file:
            file.write(f'Pesel;BirthDate;Century;Gender;Bool\n')
    return None


def collect_detailed_data_from_online_generator():
    """This function gets a PESEL with additional info ( born 'in between' and gender ) from online generator
     and adds it and its shuffled version to a csv file."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://generatorliczb.pl/generator-pesel")
    wait = WebDriverWait(driver, 15, 0.5)
    # Ze strony zniknęła informacja o cookies wiec nie ma potrzeby akceptacji ( ponizsze 4 linie zakomentowane )
    # wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Zgadzam")]')))
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Zgadzam")]')))
    # accept = driver.find_element(By.XPATH, '//*[contains(text(),"Zgadzam")]')
    # webdriver.ActionChains(driver).move_to_element(accept).click().perform()

    generate = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
    webdriver.ActionChains(driver).move_to_element(generate)

    female = driver.find_element(By.CSS_SELECTOR, 'input[id="female"]')
    male = driver.find_element(By.CSS_SELECTOR, 'input[id="male"]')
    dateinput = driver.find_element(By.CSS_SELECTOR, 'input[name="date"]')
    # generate = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
    resultarea = driver.find_element(By.CSS_SELECTOR, 'span[class="result"]')
    centuries = ((19, (1800, 1, 1), (1899, 12, 31)),
                 (20, (1900, 1, 1), (1999, 12, 31)),
                 (21, (2000, 1, 1), (2099, 12, 31)),
                 (22, (2100, 1, 1), (2199, 12, 31)),
                 (23, (2200, 1, 1), (2299, 12, 31)))
    webdriver.ActionChains(driver).scroll_to_element(generate).perform()
    webdriver.ActionChains(driver).scroll_by_amount(0, 300).perform()

    with open('detailedpesels.csv', 'a') as file:
        fake = Faker()
        for _ in range(1):  # This FOR was previously used to collect larger amount of data for a fucked-up ML project
            for i in range(5):

                date = fake.date_between(start_date=datetime(centuries[i][1][0], centuries[i][1][1],
                                                             centuries[i][1][2]),
                                         end_date=datetime(centuries[i][2][0], centuries[i][2][1],
                                                           centuries[i][2][2]))
                webdriver.ActionChains(driver).move_to_element(female).click().perform()
                gender = '0'  # added
                dateinput.send_keys(f'{date.day}.{date.month}.{date.year}')
                webdriver.ActionChains(driver).move_to_element(generate).click().perform()
                time.sleep(1.5)
                resultpesel = resultarea.text[:11]
                shuffledpesel = string_utils.shuffle(resultpesel)
                dateinput.clear()

                def writepeseltocsv(sex):
                    file.write(f'{resultpesel};{date.year}{date.month:02}{date.day:02};{centuries[i][0]};{sex};1\n')
                    file.write(f'{shuffledpesel};{date.year}{date.month:02}{date.day:02};{centuries[i][0]};{sex};0\n')
                    print(f'{resultpesel} and {shuffledpesel} added to detailedpesels.csv')
                    return None

                writepeseltocsv(gender)

                webdriver.ActionChains(driver).move_to_element(male).click().perform()
                gender = '1'  # added
                dateinput.send_keys(f'{date.day}.{date.month}.{date.year}')
                webdriver.ActionChains(driver).move_to_element(generate).click().perform()
                time.sleep(1.5)
                resultpesel = resultarea.text[:11]
                shuffledpesel = string_utils.shuffle(resultpesel)
                dateinput.clear()
                writepeseltocsv(gender)
    driver.quit()
    return None
