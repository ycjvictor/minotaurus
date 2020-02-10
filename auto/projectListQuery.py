# coding=utf-8

import time


class ProjectListQuery(object):
    def __init__(self):
        pass

    def project_list_query(self, browser, project_name=None):
        # 项目名称查询框
        project_name_box = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td[4]/input')
        project_name_box.send_keys(project_name)
        #查询按钮
        query_button = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/button[2]')
        query_button.click()
        time.sleep(2)
        # 点击查看项目详情
        check_button = browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div/div/div/div/table/tbody/tr/td[7]/span[1]')
        check_button.click()