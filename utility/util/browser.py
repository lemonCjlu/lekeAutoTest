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


  #�������ػ�������
  def StartLocalFireFoxDriver(self):
    self.driver = webdriver.Firefox()
    self.driver.maximize_window()

##  #����Զ�̻�������
  def StartRemoteFireFoxDriver(self, node_url):
    return
##    try:
##      driver = webdriver.Remote(node_url, desired_capabilities=DesiredCapabilities.FIREFOX)
##      driver.maximize_window()
##    except e:
##      Assertion.verfyEquals(e, "����chromeԶ�̽ڵ㣺" + node_url + " ʧ��")

  #��������chrome�����
  def StartLocalChromeDriver(self):
    self.driver = webdriver.Chrome(Broswer.chromedriver)
    self.driver.maximize_window()

  #����Զ��chrome�����
  def StartRemoteChromeDiver(self, node_url):
    return
##    try:
##      driver = webdriver.Remote(command_executor=url, desired_capabilities=DesiredCapabilities.CHROME)
##      driver.maximize_window()
##    except Exception, e:
##      Assertion.verfyEquals(e, "����chromeԶ�̽ڵ㣺" + node_url + " ʧ��")
      
  #��������IE�����
  def StartLocalIEDriver(self):
    self.driver = webdriver.Ie(Broswer.iedriver)#IE��ı���ģʽ�趼ѡ�ϻ򶼹���
    self.driver.maximize_window()

  #����Զ��IE�����
  def StartRemoteIEDriver(self, node_url):
    return


if __name__ == "__main__":
  B = Broswer()
  webdriver = B.GetWebDriver("chrome", None)
  webdriver.get("http://www.baidu.com")
  
