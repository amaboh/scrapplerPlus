
import os 
from selenium import webdriver 

# DRIVER_PATH = '/Users/ama/SeleniumDrivers'

os.environ['PATH'] = '/Users/ama/SeleniumDrivers'

driver = webdriver.Chrome()

driver.get("https://magento.softwaretestingboard.com/")

driver.implicitly_wait(30)
my_element = driver.find_element_by_class_name('more button')

my_element.click()

