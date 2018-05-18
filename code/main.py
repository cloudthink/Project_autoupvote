#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

class weibo_object:
    def __init__(self):
        self.driver = (webdriver.Chrome())
        self.driver.maximize_window()  # 浏览器全屏显示

    def login(self):
        self.driver.get("https://weibo.com/login.php")

        self.driver.find_element_by_name("username").send_keys("admin")
        time.sleep(3)
        self.driver.find_element_by_name("password").send_keys("passs")
        time.sleep(2)
        #self.driver.find_element_by_xpath("//span[@node-type='submitStates']")
        time.sleep(5)
        self.driver.get("https://huati.weibo.com/k/hotdog?from=501")
        while True:
            plist = self.driver.find_elements_by_xpath("//em[@class='W_ficon ficon_praised S_txt2']")
            #print(plist)
            n=200
            for one in plist:
                print(one)
                n=n+200

                time.sleep(0.1)
                try:
                    one.click()
                    time.sleep(1)
                    try:
                        self.driver.find_element_by_xpath("//a[@class='W_btn_b btn_34px'")
                        time.sleep(3)
                    except:
                        pass
                except:
                    pass
            js = "var q=document.documentElement.scrollTop=" + str(n)
            self.driver.execute_script(js)
if __name__=="__main__":
    one=weibo_object()
    one.login()