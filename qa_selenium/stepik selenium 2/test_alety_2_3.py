from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import re
import time
import pyperclip
def web_wait(browser, selector, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(selector)
    )
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'


def test_alert():
    try:
        browser.get(link)
        web_wait(browser, (By.CSS_SELECTOR, '.btn.btn-primary')).click()
        conf = browser.switch_to.alert
        conf.accept()
        x = browser.find_element(By.CSS_SELECTOR, '.nowrap#input_value').text
        x = calc(int(x))
        web_wait(browser, (By.CSS_SELECTOR, '.form-control')).send_keys(x)
        but_sub = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary').click()

        alert = browser.switch_to.alert
        text = alert.text
        alert.accept()
        num = float(re.findall(r'\d+\.?\d*', text)[0])
        pyperclip.copy(str(num))
    finally:
        browser.quit()