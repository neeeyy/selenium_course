from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
link = "http://suninjuly.github.io/simple_form_find_task.html"
stepik_link = 'https://stepik.org/lesson/138920/step/4?unit=196194'



def wait_for_css(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = wait_for_css(browser, (By.CSS_SELECTOR, '[name="first_name"]')).send_keys("VAYS")

    input2 = browser.find_element(By.CSS_SELECTOR, '[name="last_name"]')
    input2.send_keys('Petrov')

    input3 = browser.find_element(By.CSS_SELECTOR,'.form-control.city')
    input3.send_keys('Smolensk')

    input4 = browser.find_element(By.CSS_SELECTOR, '#country')
    input4.send_keys('RUSSIA')

    button = browser.find_element(By.CSS_SELECTOR, '#submit_button')
    button.click()
    
    alert = browser.switch_to.alert
    text = alert.text
    alert.accept()
    num = float(re.findall(r'\d+\.\d+', text)[0])

    browser.get(stepik_link)
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
    browser.execute_script("arguments[0].scrollIntoView(true);", input_stepik)
    input_stepik.send_keys(num)
    button_stepik = browser.find_element(By.CSS_SELECTOR, '.submit-submission')
    button_stepik.click()
finally:
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".attempt__result"),
            "Correct"
        )
    )
    browser.quit()