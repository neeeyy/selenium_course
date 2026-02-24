from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def wait_for_presence(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )

def test_registration():
    browser = webdriver.Chrome()
    link = 'https://suninjuly.github.io/registration2.html'

    try:
        browser.get(link)

        input_name = wait_for_presence(browser, (By.CSS_SELECTOR, '[placeholder="Input your name"]')).send_keys('Vasya')
        print(input_name)

       #browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your name"]').send_keys('Vasya')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]').send_keys('vasya@mail.ru')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone"]').send_keys('123456789')
        browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address"]').send_keys('улица пушкина')
        browser.find_element(By.CSS_SELECTOR, '.btn.btn-default').click()
        time.sleep(5)
        text = browser.find_element(By.TAG_NAME, 'h1').text

        assert 'Congratulations!' in text, f"Unexpected text: {text}"

    finally:
        browser.quit()