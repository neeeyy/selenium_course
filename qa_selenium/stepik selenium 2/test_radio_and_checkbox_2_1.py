from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import re
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def web_wait(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )
def web_wait_click(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )

#
def test_math():
    browser = webdriver.Chrome()
    url = 'https://suninjuly.github.io/get_attribute.html'

    try:
        browser.get(url)

        x = web_wait(browser, (By.CSS_SELECTOR, '#treasure')).get_attribute('valuex')
        x = calc(x)

        web_wait(browser, (By.CSS_SELECTOR, '#answer')).send_keys(x)
        web_wait(browser, (By.CSS_SELECTOR, '#robotCheckbox')).click()
        web_wait(browser, (By.CSS_SELECTOR, '[id="robotsRule"]')).click()
        web_wait_click(browser, (By.CSS_SELECTOR, '.btn')).click()

        alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
        text_alert = alert.text
        alert.accept()
        num = float(re.findall(r'\d+\.?\d*', text_alert)[0])  # ← Исправлена регулярка
        pyperclip.copy(str(num))
        print(f"✅ Ответ скопирован: {num}", flush=True)

    finally:
        time.sleep(2)
        browser.quit()