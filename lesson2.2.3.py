from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    x, y = int(x_element.text), int(y_element.text)

    ans = str(x + y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(ans)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
