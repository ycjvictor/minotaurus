# coding=utf-8

import time
from selenium.webdriver.common.action_chains import ActionChains


class ProjectSidebar(object):
    def __init__(self):
        pass

    def prject_sidebar(self, browser, subitem):
        # 信息搜集
        if subitem == u'信息录入':
            info_collection = browser.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/ul/li[1]/div[2]')
            ActionChains(browser).move_to_element(info_collection).perform()
            time.sleep(1)
            info_entry = browser.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div/div/div/div/div[2]/div/div/ul/li[2]')
            info_entry.click()

        # 招标文件来源项目的公告解读
        if subitem == u'公告解读':
            info_collection = browser.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/ul/li[2]/div[2]')
            ActionChains(browser).move_to_element(info_collection).perform()
            time.sleep(1)
            info_analyse = browser.find_element_by_xpath(
                '//*[@id="app"]/div/div[2]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div/div/ul/li[1]')
            info_analyse.click()