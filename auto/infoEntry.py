#coding=utf-8

from selenium import webdriver
import re
import random
import time


class InfoEntry(object):

    def __init__(self):
        pass

    def info_entry(self, browser):

        current_url = browser.current_url
        project_id = re.findall(r"projectId=(.+?)&", current_url)
        project_instance_code = re.findall(r"projectCode=(.+?)&", current_url)

        # 项目信息
        project_name = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectName"]')
        project_name.click()
        project_name.clear()
        project_name.send_keys((str(project_id[0]).encode('utf-8') + "测试项目").decode('utf-8'))
        project_cast = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectCast"]/div[2]/input')
        project_cast.send_keys(str(round(random.uniform(10000000, 50000000), 2)))

        # 获取项目类型下拉框
        project_type = browser.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div['
                                                     '1]/form/div[1]/div[2]/div/div[1]/div[3]/div/div['
                                                     '2]/div/span/div/div/div/div')
        # 呼出下拉列表
        project_type.click()

        # 测试使用: 验证是否找到目标列表
        project_type_options = browser.find_element_by_xpath("/html/body/div[2]")
        inner_html = project_type_options.get_attribute('innerHTML')
        print inner_html
        # 获取下拉列表可选项目数量
        ul_li_list = project_type_options.find_elements_by_xpath('/html/body/div[2]/div/div/div/ul/li')
        ul_li_sum = len(ul_li_list)
        print "下拉列表可选数量：ul_li_sum:" + str(ul_li_sum)

        # 选中某一个选项
        if ul_li_sum > 0:
            li_list = project_type_options.find_elements_by_xpath('/html/body/div[2]/div/div/div/ul/li[' + str(random.randint(0, ul_li_sum - 1)) + '3]')
            li_list[0].click()


        # project_address = browser.find_element_by_xpath('')
        # project_address_detail = browser.find_element_by_xpath('')
        # owner = browser.find_element_by_xpath('')
        # agency = browser.find_element_by_xpath('')
        # fund_source = browser.find_element_by_xpath('')
        # bussiness_mode = browser.find_element_by_xpath('')
        # competition_mode = browser.find_element_by_xpath('')
        # # 竞争方式选其他
        # expected_construction_period = browser.find_element_by_xpath('')
        # expected_process_time = browser.find_element_by_xpath('')
        # competitor = browser.find_element_by_xpath('')
        # technical_difficulty = browser.find_element_by_xpath('')
        # construction_condition = browser.find_element_by_xpath('')
        # payment_condition = browser.find_element_by_xpath('')
        # project_overview = browser.find_element_by_xpath('')
        #
        # # 备用机
        # reserve_fund = browser.find_element_by_xpath('')
        # reserve_fund_use = browser.find_element_by_xpath('')
        #
        # # 自我评测-投入周期计划
        # tender_stage_input_before = browser.find_element_by_xpath('')
        # tender_stage_input = browser.find_element_by_xpath('')
        # construction_stage_input = browser.find_element_by_xpath('')
        #
        # # 自我评测-收入周期计划
        # tender_stage_income_before = browser.find_element_by_xpath('')
        # tender_stage_income = browser.find_element_by_xpath('')
        # construction_stage_income = browser.find_element_by_xpath('')
        #
        # # 自我评测-拟投入资源
        # expected_input_source_time = browser.find_element_by_xpath('')
        # expected_input_source_manpower = browser.find_element_by_xpath('')
        # expected_input_source_cert = browser.find_element_by_xpath('')
        # expected_input_source_performance = browser.find_element_by_xpath('')
        # expected_input_source_honor = browser.find_element_by_xpath('')
        # expected_input_source_fund = browser.find_element_by_xpath('')
        #
        # # 自我评测-风险点
        # risk_site_enviroment = browser.find_element_by_xpath('')
        # risk_social_enviroment = browser.find_element_by_xpath('')
        # risk_technology = browser.find_element_by_xpath('')
        # risk_quality = browser.find_element_by_xpath('')
        # risk_safety = browser.find_element_by_xpath('')
        # risk_fund = browser.find_element_by_xpath('')
        # risk_policy = browser.find_element_by_xpath('')
        # risk_political = browser.find_element_by_xpath('')
        # risk_partner = browser.find_element_by_xpath('')
        #
        # # 自我评测-收益
        # income_brand = browser.find_element_by_xpath('')
        # income_team = browser.find_element_by_xpath('')
        # income_honor = browser.find_element_by_xpath('')
        # income_performance = browser.find_element_by_xpath('')
        # income_profit = browser.find_element_by_xpath('')
        #
        # # 自我评测-综合评估
        # comprehensive_eveluation = browser.find_element_by_xpath('')


# 你眼睛长哪里去了
if __name__ == "__main__":
    # print (str(47).encode('utf-8') + "测试项目").decode('utf-8')
    print round(random.uniform(10000000, 50000000), 2)
