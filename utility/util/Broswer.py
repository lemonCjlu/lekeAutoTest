# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class Broswer:
  driver = None
  chromedriver_exe = 'chromedriver.exe'
 # System.setProperty("webdriver.chrome.bin", "chromedriver.exe")

  def __init__(self, browser, node_url):
    return


  def SelectBrowser(self, browser, node_url):
    return


  #�������ػ�������
  def StartLocalFireFoxDriver(self):
    driver = webdriver.Firefox()
    driver.maximize_window()

  def StartRemoteFireFoxDriver(self, node_url):
    try:
      driver = webdriver.Remote(node_url, desired_capabilities=DesiredCapabilities.FIREFOX)
      driver.maximize_window()
    except e:
      Assertion.verfyEquals(e, "����chromeԶ�̽ڵ㣺" + node_url + " ʧ��")

  def StartLocalChromeDriver(self):
    driver = webdriver.chrome()
    driver.maximize_window()

  def StartRemoteChromeDiver(sefl, node_url):
    try:
      driver = webdriver.Remote(node_url, desired_capabilities=DesiredCapabilities.CHROME)
      driver.maximize_window()
    except e:
      Assertion.verfyEquals(e, "����chromeԶ�̽ڵ㣺" + node_url + " ʧ��")
      

  def StartLocalIEDriver(self):
    return 

  def StartRemoteIEDriver(self, node_url):
    return
