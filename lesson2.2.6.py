from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    funk = lambda x: str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = funk(x)

    ans = browser.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    check1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    check1.click()
    check2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    check2.click()


    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
