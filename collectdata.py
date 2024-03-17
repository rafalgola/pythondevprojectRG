from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testerzy.pl/baza-wiedzy/narzedzia-online/generatory")

wait = WebDriverWait(driver, 15, 0.5)
wait.until(EC.visibility_of_element_located((By.ID, 'cookieLawModal-accept')))
accept = driver.find_element(By.ID, 'cookieLawModal-accept')
webdriver.ActionChains(driver).move_to_element(accept).click().perform()

# nlas = driver.find_element(By.ID, 'newLineAsSeparator')
# webdriver.ActionChains(driver).move_to_element(nlas).click().perform()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="generate"]')))
generate = driver.find_element(By.CSS_SELECTOR, 'button[id="generate"]')
resultarea = driver.find_element(By.XPATH, '//textarea[@id="results"]')
webdriver.ActionChains(driver).move_to_element(generate).perform()
for _ in range(4):
    wait.until(EC.element_to_be_clickable(generate))
    webdriver.ActionChains(driver).click(generate).perform()
    time.sleep(1)
    textresult = resultarea.get_attribute('value')
    print("Result:", textresult)

driver.quit()
