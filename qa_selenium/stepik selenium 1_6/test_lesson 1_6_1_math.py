from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/find_link_text'
try:
    browser.get(link)
    q = str(math.ceil(math.pow(math.pi, math.e)*10000))
    find_link = browser.find_element(By.LINK_TEXT, q)
    find_link.click()
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="first_name"]')
    input1.send_keys("Vasya")
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    input2.send_keys('Petrov')
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    input3.send_keys("HABAROVSK")
    input4 = browser.find_element(By.CSS_SELECTOR, '#country')
    input4.send_keys('RUSSIA')
    btn = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    btn.click()
   # time.sleep(10)
    alert = browser.switch_to.alert
    text = alert.text
    alert.accept()
    num = float(re.findall(r'\d+\.\d+', text)[0])
    link_stepik = 'https://stepik.org/lesson/138920/step/5?unit=196194'
    browser.get(link_stepik)

    cookies = [
    {
        "name": "csrftoken",
        "value": "SS8ECLD9tK3dv4PfPdRAsSxtQACW6Rccy2QXYlNRk9LfqcnADZgCCVAwfp90amxw",
        "domain": ".stepik.org"
    },
    {
        "name": "sessionid",
        "value": "dq340utdr4c167wzikvwm9kcuyd3llcv",
        "domain": ".stepik.org"
    }
    ]

    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()
    input_stepik = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".string-quiz__textarea")
        )
    )
    browser.execute_script('arguments[0].scrollIntoView(true);', input_stepik)
    input_stepik.send_keys(num)
    but_stepik = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.submit-submission')
        )
    )
    but_stepik.click()

finally:
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".button.success"),
            "Следующий шаг"
        )
    )
    browser.quit()