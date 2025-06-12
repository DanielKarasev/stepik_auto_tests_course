from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def but():
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

try:
    link = 'https://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    but()
    confirm = browser.switch_to.alert
    confirm.accept()

    funk = lambda x: str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = funk(x)

    ans = browser.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(y)

    but()

    alert = browser.switch_to.alert
    alert_text = alert.text

    answ = alert_text.split(': ')[-1]
    print(answ)

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
