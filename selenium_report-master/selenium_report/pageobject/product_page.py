#-*-coding:utf-8-*-
from selenium import webdriver
from framework.base_page import BasePage
from framework.logger import Logger
from pageobject.login_page import LoginPage
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
import os
from framework.openbrowser import OpenBrowser
# create a logger instance
logger = Logger(logger="ProductPage").getlog()

class ProductPage(object):

    def __init__(self):
        op_br = OpenBrowser()
        self.driver = op_br.get_driver()
        self.basepage = BasePage()
        self.Login = LoginPage()
    def login(self):
        self.Login.login("http://www.yunkezan.com/admin/roomstyle/index")

    def click_product(self,productcate):
        logger.info(u"跳转到选择的产品页面")
        self.driver.get("http://www.yunkezan.com/admin/roomstyle/index")
        self.basepage.get_windows_img()
        #self.driver.find_element_by_partial_link_text(u"门票").click()
        self.driver.find_element_by_partial_link_text(productcate).click()
        self.basepage.get_windows_img()

    def create_product(self,hotelvalue,indextype):
        logger.info(u"点击创建产品")
        self.driver.find_element_by_partial_link_text(u"创建产品").click()
        self.basepage.get_windows_img()
        select = self.driver.find_element_by_id("hotelId")
        #Select(select).select_by_value("315")
        Select(select).select_by_value(hotelvalue)
        self.basepage.get_windows_img()
        #self.driver.find_element_by_xpath(".//*[@id='roomStyleTypeList']/label[2]/input").click()
        self.driver.find_element_by_xpath(self.indextype).click()
        #self.driver.find_element_by_xpath(".//*[@id='createProductModal']/div/div/div[3]/button[1]").click()
        self.driver.find_element_by_xpath(".//*[@id='createProductModal']/div/div/div[3]/button[1]").click()
    def insert_menpiao_info(self,label,productname,starttime,endtime,count,productAlias):
        try:
            self.driver.find_element_by_id("inputTag")
        except NoSuchElementException as msg:
            print  "未找到此元素%s" % msg
        else:
            logger.info(u"输入标签内容")
            self.driver.find_element_by_id("inputTag").send_keys(label)
            self.basepage.get_windows_img()

        try:
            self.driver.find_element_by_partial_link_text(u"添加")
        except NoSuchElementException as msg:
            print  "未找到此元素%s" % msg
        else:
            logger.info(u"点击添加按钮")

            self.driver.find_element_by_partial_link_text(u"添加").click()
            self.basepage.get_windows_img()
        logger.info(u"输入产品名称")
        self.driver.find_element_by_id("goodsName").send_keys(productname)

        logger.info(u"修改产品状态")
        status = self.driver.find_element_by_id("statusIs")
        Select(status).select_by_value("1")

        logger.info(u"选择开始日期")
        self.driver.find_element_by_id("presellStartTime").starttime.send_keys(starttime)

        logger.info(u"选择结束日期")
        self.driver.find_element_by_id("presellEndTime").endtime.send_keys(endtime)

        logger.info(u"可使用人数")
        self.driver.find_element_by_id("maxOccupancy").send_keys(count)

        logger.info(u"输入产品别名")
        self.driver.find_element_by_id("goodsAlias").send_keys(productAlias)
        self.basepage.get_windows_img()

    def insert_huiyishi_info(self, label, productname,count, starttime, endtime ,price,stock,location,mianji,huiyishi,productAlias):
        logger.info(u"输入标签内容")
        self.driver.find_element_by_id("inputTag").send_keys(label)
        self.basepage.get_windows_img()
        self.driver.find_element_by_partial_link_text(u"添加")
        logger.info(u"点击添加按钮")
        self.driver.find_element_by_partial_link_text(u"添加").click()
        self.get_windows_img()

        logger.info(u"输入产品名称")
        self.driver.find_element_by_id("goodsName").send_keys(productname)

        logger.info(u"修改产品状态")
        status = self.driver.find_element_by_id("statusIs")
        Select(status).select_by_value("1")

        logger.info(u"可使用人数")
        self.driver.find_element_by_id("maxOccupancy").send_keys(count)

        logger.info(u"选择开始日期")
        starttime = self.driver.find_element_by_id("presellStartTime")
        starttime.send_keys(self.starttime)

        logger.info(u"选择结束日期")
        endtime = self.driver.find_element_by_id("presellEndTime")
        endtime.send_keys(self.endtime)

        logger.info(u"输入价格")
        self.driver.find_element_by_id("price").send_keys(price)

        logger.info(u"输入库存")
        self.driver.find_element_by_id("stockNum").send_keys(stock)

        logger.info(u"输入位置")
        self.driver.find_element_by_id("location").send_keys(location)

        logger.info(u"选择面积")
        self.driver.find_element_by_name("goods[area]").send_keys(mianji)


        logger.info(u"会议室类型")
        self.driver.find_element_by_name("goods[meetingRoomType]").send_keys(huiyishi)


        logger.info(u"输入产品别名")
        self.driver.find_element_by_id("goodsAlias").send_keys(productAlias)
        self.basepage.get_windows_img()

    def insert_play_info(self,label, productname,count, starttime, endtime ,price,stock,location, productAlias):


        logger.info(u"输入标签内容")
        self.driver.find_element_by_id("inputTag").send_keys(label)
        self.basepage.get_windows_img()
        self.driver.find_element_by_partial_link_text(u"添加")

        logger.info(u"点击添加按钮")

        self.driver.find_element_by_partial_link_text(u"添加").click()


        logger.info(u"输入产品名称")
        self.driver.find_element_by_id("goodsName").send_keys(productname)

        logger.info(u"修改产品状态")
        status = self.driver.find_element_by_id("statusIs")
        Select(status).select_by_value("1")

        logger.info(u"可使用人数")
        self.driver.find_element_by_id("maxOccupancy").send_keys(self.count)

        logger.info(u"选择开始日期")
        starttime = self.driver.find_element_by_id("presellStartTime")
        starttime.send_keys(starttime)

        logger.info(u"选择结束日期")
        endtime = self.driver.find_element_by_id("presellEndTime")
        endtime.send_keys(endtime)

        logger.info(u"输入价格")
        self.driver.find_element_by_id("price").send_keys(price)

        logger.info(u"输入库存")
        self.driver.find_element_by_id("stockNum").send_keys(stock)

        logger.info(u"输入位置")
        self.driver.find_element_by_id("location").send_keys(location)
        logger.info(u"输入产品别名")
        self.driver.find_element_by_id("goodsAlias").send_keys(productAlias)
        self.basepage.get_windows_img()
    def frame_user(self,userways,usercontent,productnotice):
        logger.info(u"切换到框架使用方法")
        try:

            frame1 = self.driver.find_elements_by_class_name("ke-edit-iframe")
        except NoSuchFrameException as msg:
            print u"未找到此框架%s" % msg
        else:

            self.driver.switch_to_frame(frame1[0])

            self.driver.find_element_by_class_name("ke-content").send_keys(userways)
            self.driver.switch_to_default_content()
            self.basepage.get_windows_img()

            logger.info(u"切换到框架内容使用")
            self.driver.switch_to_frame(frame1[1])
            # self.driver.find_element_by_id("ticketUsed").send_keys(Keys.TAB)
            # self.driver.find_element_by_id("ticketUsed").click()

            self.driver.find_element_by_class_name("ke-content").send_keys(usercontent)
            self.driver.switch_to_default_content()
            self.basepage.get_windows_img()

            #logger.info(u"切换到框架套餐说明")
            self.driver.switch_to_frame(frame1[2])
            # self.driver.find_element_by_id("ticketUsed").send_keys(Keys.TAB)
            # self.driver.find_element_by_id("ticketUsed").click()

            self.driver.find_element_by_class_name("ke-content").send_keys(productnotice)
            self.driver.switch_to_default_content()
            self.basepage.get_windows_img()




    def update_img(self):

        logger.info(u"上传产品相册")
        self.driver.find_element_by_xpath(".//span[@id='j-updateopen']/div[2]/label").click()
        os.system("C:\Users\qiuyunxia.YCF\Desktop\upfile.exe")  # 你自己本地的这个.exe文件绝对路径

        logger.info(u"上传海报图")
        self.driver.find_element_by_id("inputImage").click()
        # 执行autoit上传文件
        os.system("C:\Users\qiuyunxia.YCF\Desktop\upfile.exe")  # 你自己本地的这个.exe文件绝对路径
        self.basepage.get_windows_img()
    def save(self):

        logger.info(u"点击保存按钮")
        self.driver.find_element_by_id("editsubmit").click()
        # 执行autoit上传文件
        self.basepage.get_windows_img()










