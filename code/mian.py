#-*- coding:utf-8 -*-
from selenium import webdriver
from splinter.browser import Browser

import time

#登录页
def login(onebrowser):
    b=onebrowser

    b.visit("https://weibo.com/login.php")
    time.sleep(1)

    b.fill("username","17862903881")  #填写账户密码
    time.sleep(1)
    b.fill("password","9999danchen")
    time.sleep(1)
    b.click_link_by_text("登录")
    time.sleep(1)
    mcookies=onebrowser.cookies.all()
    print(mcookies)
    return b

def pos(onebrowser):
    onebrowser.visit(
        "https://weibo.com/p/100808f6e9b8ffa0f3655b17bee6192711511c?k=%E6%B5%8E%E5%8D%97%E5%A4%A7%E5%AD%A6%E4%B9%B1%E6%94%B6%E8%B4%B9&_from_=huati_topic")
    plist=onebrowser.find_by_xpath("//a[@class='S_txt2']")
    print(plist)
    for one in plist:
        one.click()
    return onebrowser
if __name__=="__main__":
    mobile_emulation = {"deviceName": "iPad Pro"}

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    b = Browser(driver_name="chrome", options=chrome_options)  # 打开浏览器
    time.sleep(1)
    login(b)
    time.sleep(1)
    b.visit("https://weibo.com/")
    time.sleep(1)
    b=pos(b)
    print(b)