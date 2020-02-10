# coding=utf-8

from selenium import webdriver
import time
from login import Login
from infoEntry import InfoEntry
from projectListQuery import ProjectListQuery
from projectSidebar import ProjectSidebar


class AutoTester(object):

    def auto_tester(self, url, browser, acctountId, passwordId, submit, acctount, password):
        Login().login_without_qr(url, browser, acctountId, passwordId, submit, acctount, password)
        browser.get("http://47.96.183.143/#/pm/manage/project-list")
        time.sleep(1)

        # # 新建立项
        # browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/button').click()
        # # 规则权限下一步
        # time.sleep(1)
        # browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/button').click()
        # # 项目来源
        # time.sleep(1)
        # browser.find_element_by_xpath('//*[@id="sourceType"]/label[2]').click()  # 其他来源
        # # browser.find_element_by_xpath('//*[@id="sourceType"]/label[1]').click()  # 招标文件来源
        # browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]')

        ProjectListQuery().project_list_query(browser, u'47测试')
        time.sleep(1)
        ProjectSidebar().prject_sidebar(browser, u'信息录入')
        InfoEntry().info_entry(browser)

if __name__ == "__main__":
    url = "http://47.96.183.143/#/login"
    browser = webdriver.Chrome()
    acctountId = "account"
    passwordId = "password"
    acctount = "admin"
    password = "111111"
    submit = "ant-btn-lg"

    auto_tester = AutoTester()
    auto_tester.auto_tester(url, browser, acctountId, passwordId, submit, acctount, password)