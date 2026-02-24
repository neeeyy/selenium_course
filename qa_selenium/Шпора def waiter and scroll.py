from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# -------- WAIT HELPERS --------
def wait_for_clickable(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def wait_for_visible(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def wait_for_presence(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )

#auto scroll
element = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".btn")
    )
)
browser.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    element
)
element.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import re
import pyperclip

presence_of_element_located #Элемент появился в коде страницы
visibility_of_element_located #Элемент виден на экране (для чтения текста)
element_to_be_clickable #Кнопка готова к клику
alert_is_present #Ждём всплывающее окно
invisibility_of_element_located #Ждём, пока пропадёт лоадер или модалка