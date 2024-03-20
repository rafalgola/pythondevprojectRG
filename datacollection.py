from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import string_utils


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



