#-*-coding:utf-8-*-
from framework.logger import Logger
from framework.openbrowser import OpenBrowser
from framework.base_page import BasePage
# create a logger instance
logger = Logger(logger="LoginPage").getlog()
class LoginPage(object):
    def __init__(self):
        #self.basepage = BasePage()
        op_br = OpenBrowser()
        self.driver = op_br.get_driver()

    def login(self,url):
        logger.info(u"登录")
        self.driver.get(url)
        self.driver.add_cookie({'name': 'PHPSESSID', 'value': "kd4pf91tk3nki4jrv9dqltjoq3"})
        self.driver.add_cookie(
            {'name': 'Hm_lvt_b4f24f7a55688ef9106fe15ce9843d2a', 'value': '1515550025,1515721314,1515810121,1515980452'})
        self.driver.add_cookie({'name': 'Hm_lpvt_b4f24f7a55688ef9106fe15ce9843d2a', 'value': 'time()'})

        self.driver.refresh()
        self.driver.maximize_window()




















