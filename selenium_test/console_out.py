from time import sleep

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#
# capabilities = DesiredCapabilities.CHROME
# capabilities['loggingPrefs'] = { 'browser':'ALL' }
#
driver = webdriver.Chrome()

driver.get('http://localhost:3333')

sleep(5)
# print console log messages
for entry in driver.get_log('browser'):
    print(entry)