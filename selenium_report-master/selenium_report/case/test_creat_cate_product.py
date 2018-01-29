#-*-coding:utf-8-*-
from selenium import webdriver
from framework.logger import Logger
import unittest
from pageobject.product_page import ProductPage
# create a logger instance
logger = Logger(logger="Creat_Product").getlog()
class Creat_Product(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        logger.info("Open browser")
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')


        # 打开chrome浏览器
        cls.driver = webdriver.Chrome(chrome_options=option)
        """browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)"""

    @classmethod
    def tearDownClass(cls):
        logger.info("Quit browser")
        cls.driver.quit()
    def test_ticket(self):
        login = ProductPage(self.driver)
        #login.login()
        login.click_product("门票")
        login.create_product("315",".//*[@id='roomStyleTypeList']/label[2]/input")
        login.insert_menpiao_info(u"产品名称测试1234",u"标签测试产品名称",u"2018-01-15",u"2018-01-20",4,u"产品别名")
        login.frame_user(u"使用方法",u"使用说明",u"套餐说明")
        login.update_img()
        login.save()


if __name__ == "__main__":
    unittest.main()






