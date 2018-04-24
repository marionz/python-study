from selenium import webdriver
from selenium.webdriver.common.by import By
from my_python import log_util

import time

log_util.setup_log_and_return_log_file()

firefox_driver = webdriver.Firefox()
try:
    firefox_driver.get("http://www.baidu.com/")
    firefox_driver.find_element_by_id('kw').send_keys("Python")
    firefox_driver.find_element_by_id('su').click()
    time.sleep(3)
    nums_text = firefox_driver.find_element(By.CLASS_NAME, 'nums').text
    assert '百度为您找到相关结果约100,000,000个' != nums_text
    time.sleep(1)
finally:
    firefox_driver.quit()








