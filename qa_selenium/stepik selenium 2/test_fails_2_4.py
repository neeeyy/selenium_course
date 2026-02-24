from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pyperclip
import re
browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/file_input.html'
browser.get(link)
input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Vasya')
input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Petrov')
input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('Vasya@mail.ru')
file_load = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
file_load.send_keys(file_path)
btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

alert = browser.switch_to.alert
text = alert.text
alert.accept()
num = float(re.findall(r'\d+\.?\d*', text)[0])
pyperclip.copy(str(num))
browser.quit()