#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from openbrowser import OpenBrowser

class FindElement(object):
    def __init__(self):
        open_browser = OpenBrowser()
        self.driver = open_browser.get_driver()
    def find_Element_By_Id(self, element):
        try:
            return self.driver.find_element_by_id(str(element))
        except NoSuchElementException as msg:
            print u"查找元素异常%s"%msg

    def find_Element_By_Class(self, element):
        try:
            return self.driver.find_element_by_class_name(str(element))
        except NoSuchElementException as msg:
            print u"查找元素异常%s"%msg

    def find_Element_By_Name(self, element):
         try:
            return self.driver.find_element_by_name(str(element))
         except NoSuchElementException as msg:
             print u"查找元素异常%s" % msg

    def find_Element_By_Tag_Name (self, element):
        try:
            return self.driver.find_element_by_tag_name(str(element))
        except NoSuchElementException as msg:
            print u"查找元素异常%s"%msg

    def find_Element_By_Xpath(self, element):
        try:
            return self.driver.find_element_by_xpath(str(element))
        except NoSuchElementException as msg:
            print u"查找元素异常%s"%msg


    def find_Element_By_Link_Text(self, element):
        try:
            return self.driver.find_element_by_link_text(str(element))
        except NoSuchElementException as msg:
            print u"查找元素异常%s"%msg


    def find_Element_By_Partial_Link_Text(self, element):
        try:
            return self.driver.find_element_by_partial_link_text(str(element))
        except NoSuchElementException as msg:
            print u"查找元素异常%s" % msg

    """def scroll(self, top=math.random.randint(100, 999)):
        topsize = top
        js = "var q=document.documentElement.scrollTop=" + str(topsize)
        return self.driver.execute_script(js)"""


    def get_Current_Url(self):
        return self.driver.current_url


    def set_Time_Out(self,times="60"):
        return self.driver.implicitly_wait(times)

    @staticmethod
    def setMaxWindow(self):
        return self.driver.maximize_window()