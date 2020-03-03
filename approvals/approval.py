# coding=utf-8

import random
import datetime
from util.SelectorUtils import SelectorUtils


class Approval(object):
    def __init__(self, ):
       pass

    def approval_base_info(self, browser, approval_result, approval_opinion):
        # 审批结果
        # 定价、废标等审批没有同意或不同意
        if approval_result is None:
            pass
        # 同意
        elif approval_result == 1:
            agree_result = browser.find_element_by_xpath('//*[@id="approvalResult"]/label[1]/span[1]/input')
            agree_result.click()
        # 不同意
        elif approval_result == 2:
            disagree_result = browser.find_element_by_xpath('//*[@id="approvalResult"]/label[2]/span[1]/input')
            disagree_result.click()

        # 审批意见
        approval_opinion_box = browser.find_element_by_xpath('//*[@id="approvalOpinion"]')
        approval_opinion_box.send_keys(approval_opinion)

    def approval_submit_button(self, browser):
        # 提交审批
        submit_button = browser.find_element_by_css_selectot('html body div#app div.app-wrapper '
                                                             'div.app-wrapper-content div.oa div.oa-main '
                                                             'div.container.container-oa div.container-footer '
                                                             'div.footer-button button.mr8.ant-btn.ant-btn-primary')
        browser.execute_script('arguments[0].click()', submit_button )

    # 信息评审经办人指派
    def manager_designate(self, browser, is_changed):
        """
        :param browser: 浏览器
        :param ischanged: 是否更换项目经办人（0：否； 1：是）
        """
        if is_changed == 0:
            pass

        # 经办人选择元素
        if is_changed == 1:
            manager_box = browser.find_element_by_xpath('//*[@id="projectManagerId"]/div/div')
            origin_manager = manager_box.getText()

            manager_box.click()
            manager_box_ops = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li')
            manager_ops_sum = len(manager_box_ops)

            while 1:
                ran_num = str(random.randint(1, manager_ops_sum))
                option = browser.find_element_by_xpath('/html/body/div[3]/div/div/div/ul/li[' + ran_num + ']')
                if option[0].text != origin_manager:
                    browser.execute_script('arguments[0].click()', option[0])
                    break

    # 踏勘指派
    def exploration_designate(self, browser, is_explore):
        exploration_box = browser.find_element_by_xpath('//*[@id="isSurveyed"]/div/div')
        exploration_box.click()

        # 不踏勘
        if is_explore == 0:
            false_option = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[2]')
            browser.execute_script('arguments[0].click()', false_option)

        # 踏勘
        else:
            true_option = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/ul/li[1]')
            browser.exexcute_script('arguments[0].click()', true_option)

            # 踏勘负责人
            exploration_lead_lcation = '//*[@id="principalId"]/div/div'
            exploration_lead_ops_lcation = '/html/body/div[5]/div/div/div/ul/li'
            SelectorUtils().selector_choose(browser, exploration_lead_lcation, exploration_lead_ops_lcation)

            # 踏勘参与人
            exploration_participant_lcation = '//*[@id="personId"]/div/div'
            exploration_participant_ops_lcation = '/html/body/div[6]/div/div/div/ul/li'
            SelectorUtils.selector_choose(browser, exploration_participant_lcation, exploration_participant_ops_lcation)

            # 踏勘时间
            exploration_time_location = browser.find_element_by_xpath('//*[@id="surveyedTime"]/div/input')
            # js去掉readonly属性
            # remove_readonly_js = '$(".ant-calendar-input").attr("readonly",false)'
            # browser.execute_script(remove_readonly_js)

            # # now_time = datetime.datetime.now()
            # # today = datetime.datetime.strftime(now_time, '%Y-%m-%d')
            # today = datetime.date.today()
            # tomorrow = today + datetime.timedelta(days=1)

            # exploration_time_location.send_keys(tomorrow)


    # TODO: 公告解读审批标书指派
    def tenter_book_designate(self):
        pass

    # TODO: 定价审批报价填写
    def price_quote(self):
        pass