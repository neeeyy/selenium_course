from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
import re
import math
import pyperclip
import time

def web_wait(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        ES.visibility_of_element_located(locator)
    )

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def test_result():
    print("🚀 НАЧАЛО ТЕСТА", flush=True)
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    try:
        browser.get(link)
        num = web_wait(browser, (By.CSS_SELECTOR, '.form-group #input_value')).text
        num = int(num)
        answ = calc(num)
        input1 = browser.find_element(By.CSS_SELECTOR, '#answer')

# ПРимер использования JS, визуальный переход к элементу
        browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
        input1.send_keys(answ)
        web_wait(browser, (By.CSS_SELECTOR, '#robotCheckbox')).click()
        web_wait(browser, (By.CSS_SELECTOR, '#robotsRule')).click()
        web_wait(browser, (By.CSS_SELECTOR, '.btn.btn-primary')).click()

        alert = browser.switch_to.alert
        text = alert.text
        alert.accept()
        num = float(re.findall(r'\d+\.?\d*', text)[0])
        pyperclip.copy(str(num))
        print(f"✅ Ответ скопирован: {num}", flush=True)

    finally:
        time.sleep(2)
        browser.quit()

