# -*- coding:UTF-8 -*-
'''
aaa
'''
import time
from bs4 import BeautifulSoup
from selenium import webdriver

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
    JIA = 1

    while True:
        TEXTS = DRIVER.find_elements_by_css_selector(
            "div.content.singlePage div p")
        for each_text in TEXTS:
            inner_text = DRIVER.execute_script(
                "return arguments[0].innerText;", each_text)
            print(inner_text + '\n')
            #break

        #只有第一次需要“加载更多”
        if JIA <= 1:
            flod_button = DRIVER.find_element_by_xpath(
                "//span[@class='fold-arrow-lower']")  # TODO 找不到会报错，尝试解决
            flod_button.click()
            JIA = 2
        #下一页
        nextpage = DRIVER.find_element_by_xpath(
            "//div[@class='x-page next']")   # TODO 找不到会报错，尝试解决
        if nextpage:
            print('==========next page==========\n')
            DRIVER.execute_script(
                'arguments[0].scrollIntoView(false);', nextpage)  # 拖动到可见的元素去
            nextpage.click()
            time.sleep(3)
        else:
            break
