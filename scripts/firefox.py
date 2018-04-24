import time
from my_selenium.webdriver import Remote

driver = Remote(command_executor='http://172.17.0.1:4444/wd/hub',
		desired_capabilities={
					'platform': 'ANY',
					'browserName': 'firefox'
				     }
               )
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("remote")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()
