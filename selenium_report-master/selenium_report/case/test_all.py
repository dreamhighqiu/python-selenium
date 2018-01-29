#-*-coding:utf-8-*-
from selenium import webdriver
from framework.base_page import BasePage
from framework.logger import Logger
from pageobject.login_page import LoginPage
import unittest
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from pageobject.product_page import ProductPage
import os
#import selenium_report.HTMLTestRunner_jpg
import time
import HTMLTestRunner



# create a logger instance
logger = Logger(logger="Creat_Product1").getlog()
class Creat_Product1(unittest.TestCase):
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
    def test_play(self):

        login = ProductPage(self.driver)
        login.click_product("娱乐")
        login.create_product("315",".//*[@id='roomStyleTypeList']/label[4]/input")
        login.insert_play_info(u"产品名称测试1234",u"标签测试产品名称",4,u"2018-01-15",u"2018-01-20",1,100,u"位置",u"产品别名")
        login.frame_user(u"使用方法",u"使用说明",u"套餐说明")
        login.update_img()
        login.save()
        

    def test_huiyi(self):
        login = ProductPage(self.driver)
        login.login()
        login.click_product("会议")
        login.create_product("315",".//*[@id='roomStyleTypeList']/label[5]/input")
        login.insert_huiyishi_info(u"产品名称测试1234",u"标签测试产品名称",4,u"2018-01-15",u"2018-01-20",1,100,u"位置",10,u"会议室类型",u"产品别名")
        login.frame_user(u"使用方法",u"使用说明",u"套餐说明")
        login.update_img()
        login.save()

    def test_ticket(self):
        login = ProductPage(self.driver)
        login.click_product("门票")
        login.create_product("315",".//*[@id='roomStyleTypeList']/label[2]/input")
        login.insert_menpiao_info(u"产品名称测试1234",u"标签测试产品名称",u"2018-01-15",u"2018-01-20",4,u"产品别名")
        login.frame_user(u"使用方法",u"使用说明",u"套餐说明")
        login.update_img()
        login.save()




'''if __name__ == "__main__":
    # 导入HTMLTestRunner库，这句也可以放在脚本开头
    from HTMLTestRunner import HTMLTestRunner

    # 定义脚本标题，加u为了防止中文乱码

    report_title = u'登陆模块测试报告'

    # 定义脚本内容，加u为了防止中文乱码
    desc = u'博客园登陆模块测试报告详情：'

    # 定义date为日期，time为时间
    date = time.strftime("%Y%m%d")
    time = time.strftime("%Y%m%d%H%M%S")

    # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    #path = 'D:/PyCharm/selenium_report-master/selenium_report/test_report' + date + "/login/" + time + "/"

    # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    report_path = 'D:/PyCharm/selenium_report-master/selenium_report/test_report'+ "/report.html"

    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

        # 定义一个测试容器
    testsuite = unittest.TestSuite()

    # 将测试用例添加到容器
    testsuite.addTest(Creat_Product1("test_ticket"))
    testsuite.addTest(Creat_Product1("test_play"))
    testsuite.addTest(Creat_Product1("test_huiyi"))



    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)'''
testsuite = unittest.TestSuite()
testsuite.addTest(Creat_Product1("test_ticket"))
testsuite.addTest(Creat_Product1("test_play"))
testsuite.addTest(Creat_Product1("test_huiyi"))



if __name__=='__main__':
    #执行用例
    runner=unittest.TextTestRunner()
    runner.run(suite)


