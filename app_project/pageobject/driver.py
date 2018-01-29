#-*-coding:utf-8-*-
from appium import webdriver
class Open_Driver():
    def launchapp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'GWYGL17915000053'
        desired_caps['appPackage'] = 'com.yaochufa.app'
        desired_caps['appActivity'] = '.MainTabActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    def quitdriver(self):
        self.driver.quit()

if __name__ == "__main__":
    driver = Open_Driver()
    driver.launchapp()
    driver.quitdriver()

