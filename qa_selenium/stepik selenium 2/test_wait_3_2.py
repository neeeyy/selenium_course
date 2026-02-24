from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import math
import pyperclip
def web_wait(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

def test_web_wait():
    try:
        browser.get(link)
        x = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '#price'),  # ← Локатор элемента
                "100"  # ← Ожидаемый текст
            )
        )
        web_wait(browser, (By.CSS_SELECTOR, '#book')).click()
        x = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
        x = calc(int(x))
        web_wait(browser, (By.CSS_SELECTOR, '.form-control')).send_keys(x)
        web_wait(browser, (By.CSS_SELECTOR, '#solve')).click()
        alert = browser.switch_to.alert
        text = alert.text
        alert.accept()
        num = float(re.findall(r'\d+\.?\d*', text)[0])
        pyperclip.copy(str(num))
    finally:
        browser.quit()