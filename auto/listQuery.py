# coding=utf-8

import time
from selenium.webdriver.common.keys import Keys


class ListQuery(object):

    # 项目列表查询
    def project_list_query(self, browser, project_name=None):
        if project_name is None:
            pass
        else:
            # 项目名称查询框
            project_name_box = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div['
                                                             '2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td['
                                                             '4]/input')
            project_name_box.send_keys(project_name)
        #查询按钮
        query_button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div['
                                                     '1]/div[1]/div/div[2]/button[2]')
        query_button.click()
        time.sleep(2)
        # 点击查看项目详情
        check_button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div['
                                                     '1]/div[3]/div/div/div/div/div/div/div/div/table/tbody/tr/td['
                                                     '7]/span[1]')
        check_button.click()

    # 项目通知列表查询
    def notice_list_query(self, browser, project_name=None, project_process=None):
        # OA菜单栏:项目通知
        project_notice_bar = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div')
        project_notice_bar.click()
        time.sleep(2)

        # 项目名称下拉框
        if project_name is None:
            pass
        else:
            project_name_box = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div['
                                                             '2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td['
                                                             '2]/div/div[1]/div/div')
            # 方法一：下拉查询框输入项目名称匹配（需保证输入内容得到唯一正确结果）
            project_name_box.click()
            project_name.send_keys(project_name)
            project_name.send_keys(Keys.ENTER)
            project_name_op = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div['
                                                             '2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td['
                                                             '2]/div/div[2]/div/div/div/ul/li[1]')
            browser.execute_script('arguments[0].click()', project_name_op[0])

            # # 方法二：实例的project_name需与选项文案完全一致
            # project_name_ops = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div['
            #                                                  '2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td['
            #                                                  '2]/div/div[2]/div/div/div/ul/li')
            # name_ops_sum = len(project_name_ops)
            #
            # for i in range(0, name_ops_sum):
            #     option = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div['
            #                                            '2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td['
            #                                            '2]/div/div[2]/div/div/div/ul/li[' + i + ']')
            #     if option[0].text == project_name:
            #         browser.execute_script('arguments[0].click()', option[0])
            #     break

        # 项目类型下拉框选择
        if project_process is None:
            pass
        else:
            project_process_box = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div['
                                                                '2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td['
                                                                '4]/div/div/div/div')
            project_process_box.click()
            project_process_ops = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div['
                                                                '2]/div/div[1]/div[1]/div/div[1]/table/tbody/tr[1]/td['
                                                                '4]/div/div[2]/div/div/div/ul/li')
            process_ops_sum = len(project_process_ops)

            for i in range(0, process_ops_sum):
                option = browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div['
                                                       '1]/div[1]/div/div[1]/table/tbody/tr[1]/td[4]/div/div['
                                                       '2]/div/div/div/ul/li[' + i + ']')
                if option[0].text == project_process:
                    browser.execute_script('arguments[0].click()', option[0])
                    break

        # 查询按钮
        query_button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[2]/div/div['
                                                     '1]/div[1]/div/div[2]/button[2]')
        query_button.click()
        time.sleep(2)

        # 查看通知详情
        check_button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[2]/div/div['
                                                     '1]/div[3]/div/div/div/div/div/div/table/tbody/tr[1]/td[7]/a')
        check_button.click()