# -*- coding: cp936 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities



class Broswer:
  
  chromedriver = 'chromedriver.exe'
  iedriver = 'IEDriverServer.exe'
 # System.setProperty("webdriver.chrome.bin", "chromedriver.exe")

  def __init__(self):
    self.driver = None
      
    

  def GetWebDriver(self, browser, node_url):
    print 1
    try:
      self.SelectBrowser(browser, node_url)
    except Exception, e:
      print(e)
    return self.driver
    
  def SelectBrowser(self, browser, node_url):
    if browser == "IE" and node_url == None: 
      self.StartLocalIEDriver()
    elif browser == "IE" and node_url != None:
      self.StartRemoteIEDriver(node_url)
    elif browser == "chrome" and node_url == None:
      self.StartLocalChromeDriver()
    elif browser == "IE" and node_url != None:
      self.StartRemoteChromeDiver(node_url)
    elif browser == "Firefox" and node_url == None:
      self.StartLocalFireFoxDriver()
    elif browser == "IE" and node_url != None:
      self.StartRemoteFireFoxDriver(node_url)
    else:
      print("ERROR: No this type of browser")


  #启动本地火狐浏览器
  def StartLocalFireFoxDriver(self):
    self.driver = webdriver.Firefox()
    self.driver.maximize_window()

##  #启动远程火狐浏览器
  def StartRemoteFireFoxDriver(self, node_url):
    return
##    try:
##      driver = webdriver.Remote(node_url, desired_capabilities=DesiredCapabilities.FIREFOX)
##      driver.maximize_window()
##    except e:
##      Assertion.verfyEquals(e, "启动chrome远程节点：" + node_url + " 失败")

  #启动本地chrome浏览器
  def StartLocalChromeDriver(self):
    self.driver = webdriver.Chrome(Broswer.chromedriver)
    self.driver.maximize_window()

  #启动远程chrome浏览器
  def StartRemoteChromeDiver(self, node_url):
    return
##    try:
##      driver = webdriver.Remote(command_executor=url, desired_capabilities=DesiredCapabilities.CHROME)
##      driver.maximize_window()
##    except Exception, e:
##      Assertion.verfyEquals(e, "启动chrome远程节点：" + node_url + " 失败")
      
  #启动本地IE浏览器
  def StartLocalIEDriver(self):
    self.driver = webdriver.Ie(Broswer.iedriver)#IE里的保护模式需都选上或都勾掉
    self.driver.maximize_window()

  #启动远程IE浏览器
  def StartRemoteIEDriver(self, node_url):
    return


if __name__ == "__main__":
  B = Broswer()
  webdriver = B.GetWebDriver("chrome", None)
  webdriver.get("http://www.baidu.com")
  
