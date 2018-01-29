# _*_ coding: utf-8 _*_
from selenium import webdriver
class OpenBrowser(object):
    def get_driver(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')

        # 打开chrome浏览器
        self.driver = webdriver.Chrome(chrome_options=option)
        return self.driver
if __name__ ==  '__main__':
    open_driver = OpenBrowser()
    driver = open_driver.get_driver()
    driver.get("http:www.baidu.com")
    print driver.current_url

