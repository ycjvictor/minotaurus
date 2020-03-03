# coding=utf-8

from selenium import webdriver
import time
from login import Login
from projectBuild import ProjectBuild
from infoEntry import InfoEntry
from listQuery import ListQuery
from projectSidebar import ProjectSidebar
from approvals.approvalProcess import ApprovalProcess


class AutoTester(object):

    def auto_tester(self, browser, account, password, project_source):
        #登录
        Login().login_without_qr(browser, account, password)

        #切换到项目管理模块
        # browser.get("http://47.96.183.143/#/pm/manage/project-list")
        project_oa_box = browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div')
        project_oa_box.click()
        project_option = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[5]/div/div/div/ul/li[2]')
        project_option.click()
        time.sleep(1)

        # 新建立项
        ProjectBuild().project_build(browser, project_source)
        # 其他来源
        if project_source == 1:
            # 信息录入
            InfoEntry().info_entry(browser)

        # 招标文件来源
        elif project_source == 2:
            # TODO：公告解读
            pass

        # # 项目列表查询项目进入详情
        # ListQuery().project_list_query(browser, u'61测试')
        # time.sleep(2)
        # ProjectSidebar().prject_sidebar(browser, u'信息录入')
        # time.sleep(1)
        # browser.find_element_by_xpath('//*[@id="sourceType"]/label[2]').click()  # 其他来源
        # # browser.find_element_by_xpath('//*[@id="sourceType"]/label[1]').click()  # 招标文件来源
        # browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]')

        # 信息录入并发起审批
        InfoEntry().info_entry(browser)

        # TODO: 审批
        ApprovalProcess().info_entry_approval()




if __name__ == "__main__":
    # options = webdriver.ChromeOptions()
    # options.debugger_address = "127.0.0.1:9222"
    # browser = webdriver.Chrome(options=options)
    browser = webdriver.Chrome()

    account = "akuang"
    password = "123456"
    browser.delete_all_cookies()
    auto_tester = AutoTester()
    auto_tester.auto_tester(browser, account, password, 1)


