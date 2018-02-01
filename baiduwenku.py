# -*- coding:UTF-8 -*-
'''
selenium使用demo, 为webdriver设置header,自带选择器/BeautifulSoup选择器的使用，自带选择器异常处理
'''
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

if __name__ == '__main__':
    OPT = webdriver.ChromeOptions()
    OPT.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) \
    AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    DRIVER = webdriver.Chrome(chrome_options=OPT)  # 1111
    DRIVER.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')

    MYHTML = DRIVER.page_source
    BF1 = BeautifulSoup(MYHTML, 'lxml')
    TITLE = BF1.select("div.doc-title")[0].string
    print('文章标题：%s' % TITLE)
    MORE_FLAG = 1

    while True:
        TEXTS = DRIVER.find_elements_by_css_selector("div.content.singlePage div p")
        for each_text in TEXTS:
            inner_text = DRIVER.execute_script("return arguments[0].innerText;", each_text)
            print(inner_text + '\n')
            #break # 为了快速调试，只打印每页第一行

        #只有第一次需要“加载更多”
        if MORE_FLAG <= 1:
            MORE_BTN = DRIVER.find_element_by_xpath("//span[@class='fold-arrow-lower']")
            MORE_BTN.click()
            MORE_FLAG = 2
        #下一页
        try:
            NEXT_PG = DRIVER.find_element_by_xpath("//div[@class='x-page next']")   # 找不到会报错，添加异常处理
        except NoSuchElementException as msg:
            print(u"查找元素异常%s"%msg)
            break
        else:
            #print('==========next page==========\n')
            DRIVER.execute_script('arguments[0].scrollIntoView(false);', NEXT_PG)  # 拖动到可见的元素去
            NEXT_PG.click()
            time.sleep(3)
    #print(u"程序结束。")
