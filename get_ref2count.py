from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import re

def get_wikipedia_ref2count(url):
    chromedriver_path = '/opt/homebrew/bin/chromedriver'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # GUIなし有効にする
    chrome_options.add_argument('--no-sandbox') # Headless_modeでの動作を補助（というか、エラー回避）
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url)
    element = driver.find_element(By.XPATH, '//*')
    element_text = element.text
    driver.quit()
    numbers_in_brackets = re.findall(r'\[(\d+)\]', element_text)
    return len(numbers_in_brackets)