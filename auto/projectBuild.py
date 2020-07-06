# coding=utf-8

import time


class ProjectBuild(object):
    def project_build(self, browser, project_source):
        # 新建立项
        browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/button').click()
        time.sleep(1)

        # 规则权限下一步
        next_button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[3]/div/button')
        browser.execute_script('arguments[0].click()', next_button)
        time.sleep(2)

        # 项目来源选择
        # 项目来源确认按钮
        project_source_confirm_button = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div['
                                                                    '3]/div/button[2]')
        # 其他来源
        if project_source == 1:
            browser.find_element_by_xpath('//*[@id="sourceType"]/label[2]').click()
            browser.execute_script('arguments[0].click()', project_source_confirm_button)
            time.sleep(2)

        # 招标文件来源
        elif project_source == 2:
            browser.find_element_by_xpath('//*[@id="sourceType"]/label[1]').click()
            browser.execute_script('arguments[0].click()', project_source_confirm_button)
            time.sleep(2)

        else:
            print('项目来源错误')