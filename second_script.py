from selenium import webdriver
from selenium.webdriver.common.by import By
import time

time.sleep(5)
browser = webdriver.Chrome()
time.sleep(5)
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
time.sleep(5)
button = browser.find_element(By.ID, "submit_button")
time.sleep(5)
browser.quit()
