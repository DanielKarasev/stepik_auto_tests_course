from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    funk = lambda x: str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = funk(x)

    ans = browser.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(y)

    check1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    check1.click()
    check2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    check2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
