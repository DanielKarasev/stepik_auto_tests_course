from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def but():
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    but()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

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
