from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from datetime import datetime
import string_utils
from faker import Faker


def collect_data_from_online_generator():
    """This function gets a PESEL from online generator and adds it and its shuffled version to a csv file."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://testerzy.pl/baza-wiedzy/narzedzia-online/generatory")

    wait = WebDriverWait(driver, 15, 0.5)
    wait.until(EC.visibility_of_element_located((By.ID, 'cookieLawModal-accept')))
    # wait.until(EC.element_to_be_clickable((By.ID, 'cookieLawModal-accept')))
    accept = driver.find_element(By.ID, 'cookieLawModal-accept')
    webdriver.ActionChains(driver).move_to_element(accept).click().perform()

    # nlas = driver.find_element(By.ID, 'newLineAsSeparator')
    # webdriver.ActionChains(driver).move_to_element(nlas).click().perform()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="generate"]')))
    generate = driver.find_element(By.CSS_SELECTOR, 'button[id="generate"]')
    resultarea = driver.find_element(By.XPATH, '//textarea[@id="results"]')
    webdriver.ActionChains(driver).move_to_element(generate).perform()
    with open('pesels.csv', 'a') as file:
        for _ in range(100):
            wait.until(EC.element_to_be_clickable(generate))
            webdriver.ActionChains(driver).click(generate).perform()
            time.sleep(1.5)
            resultpesel = resultarea.get_attribute('value')
            shuffledpesel = string_utils.shuffle(resultpesel)
            file.write(f'{resultpesel};1\n')
            file.write(f'{shuffledpesel};0\n')
            print(f'{resultpesel} and {shuffledpesel} added to pesels.csv.')
    driver.quit()
    return None


def collect_more_detailed_data_from_online_generator():
    """This function gets a PESEL with additional info ( born 'in between' and gender ) from online generator
     and adds it and its shuffled version to a csv file."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://generatorliczb.pl/generator-pesel")

    wait = WebDriverWait(driver, 15, 0.5)
    # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[aria-label="Zgadzam się"]')))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(), "Zgadzam")]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Zgadzam")]')))
    # wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Zgadzam się"]')))
    # wait.until(EC.element_to_be_clickable((By.ID, 'cookieLawModal-accept')))
    accept = driver.find_element(By.XPATH, '//*[contains(text(),"Zgadzam")]')
    webdriver.ActionChains(driver).move_to_element(accept).click().perform()

    female = driver.find_element(By.CSS_SELECTOR, 'input[id="female"]')
    male = driver.find_element(By.CSS_SELECTOR, 'input[id="male"]')
    date = driver.find_element(By.CSS_SELECTOR, 'input[name="date"]')
    generate = driver.find_element(By.CSS_SELECTOR, 'button[type="button"]')
    resultarea = driver.find_element(By.CSS_SELECTOR, 'span[class="result"]')

    webdriver.ActionChains(driver).scroll_to_element(female).perform()
    webdriver.ActionChains(driver).move_to_element(female).click().perform()
    webdriver.ActionChains(driver).scroll_by_amount(0, 400).perform()
    fake = Faker()

    with open('detailedpesels.csv', 'a') as file:
        for _ in range(2):
            date_to_provide = fake.date_between(start_date=datetime(1800, 1, 1), end_date=datetime(1899, 12, 31))
            date.send_keys(f'{date_to_provide.day}.{date_to_provide.month}.{date_to_provide.year}')
            webdriver.ActionChains(driver).move_to_element(generate).click().perform()
            time.sleep(1.5)
            resultpesel = resultarea.text[:11]
            shuffledpesel = string_utils.shuffle(resultpesel)
            date.clear()
            file.write(f'{resultpesel};0;1;1\n')
            file.write(f'{shuffledpesel};0;1;0\n')
            print(f'{resultpesel} and {shuffledpesel} added to detailedpesels.csv.')




    # webdriver.ActionChains(driver).move_to_element(female).click().perform()

                # {"06812381452","male born between 1800-1899. "},
                # {"43110786857","male born between 1900-1999. "},
                # {"16222947115","male born between 2000-2099. "}, //on Feb 29th.
                # {"39513017959","male born between 2100-2199. "},
                # {"82690975378","male born between 2200-2299. "},
                # {"65851742147","female born between 1800-1899. "},
                # {"91122186282","female born between 1900-1999. "},
                # {"58222753400","female born between 2000-2099. "},
                # {"13501954464","female born between 2100-2199. "},
                # {"91681510964","female born between 2200-2299. "},


    time.sleep(10)

    # resultarea = driver.find_element(By.XPATH, 'span.result')
    # webdriver.ActionChains(driver).move_to_element(generate).perform()
    # with open('pesels.csv', 'a') as file:
    #     for _ in range(100):
    #         wait.until(EC.element_to_be_clickable(generate))
    #         webdriver.ActionChains(driver).click(generate).perform()
    #         time.sleep(1.5)
    #         resultpesel = resultarea.get_attribute('value')
    #         shuffledpesel = string_utils.shuffle(resultpesel)
    #
    driver.quit()
    return None
