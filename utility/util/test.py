from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("chromedriver.exe")
#driver.get('http://www.baidu.com')
driver.maximize_window()

