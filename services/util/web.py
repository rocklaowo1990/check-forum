from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def get(url: str):
    if not 'http' in url:
        return None
    options = Options()
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # option.add_experimental_option('useAutomationExtension', False)
    # option.add_argument(
    #     'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    # )
    # option.add_argument("--disable-blink-features=AutomationControlled")
    # options.page_load_strategy = 'normal'
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        driver.get(url)

    except:
        return None

    # try:
    #     WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.TAG_NAME, 'table')))
    # except:
    #     return None

    return driver
