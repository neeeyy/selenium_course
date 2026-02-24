from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import Select
import re
import math
import pyperclip
browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/selects1.html'

def web_wait(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        ES.visibility_of_element_located(locator)
    )

def test_result():
    try:
        browser.get(link)
        num1 = web_wait(browser, (By.CSS_SELECTOR, '#num1')).text
        num2 = web_wait(browser, (By.CSS_SELECTOR, '#num2')).text
        sum_num = str(int(num1) + int(num2))
        select = Select(browser.find_element(By.CSS_SELECTOR, '.custom-select'))
        select.select_by_value(sum_num)
        web_wait(browser, ((By.CSS_SELECTOR, ".btn"))).click()

        alert = browser.switch_to.alert
        text = alert.text
        alert.accept()
        num = float(re.findall(r'\d+\.?\d*', text)[0])
        pyperclip.copy(str(num))
        print(f"✅ Ответ скопирован: {num}", flush=True)
    finally:
        browser.quit()
