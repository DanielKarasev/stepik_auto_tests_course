from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
        )
    button = browser.find_element(By.CSS_SELECTOR, "button#book")
    button.click()

    funk = lambda x: str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = funk(x)

    ans = browser.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button#solve")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text

    answ = alert_text.split(': ')[-1]
    print(answ)

finally:
    browser.quit()
