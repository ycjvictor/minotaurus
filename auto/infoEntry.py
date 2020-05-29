#coding=utf-8

from selenium import webdriver
import re
import random
import time
import datetime
from util.SelectorUtils import SelectorUtils
from selenium.webdriver.common.keys import Keys

project_id = 0


class InfoEntry(object):

    def __init__(self):
        pass

    def project_common_info(self, browser):
        current_url = browser.current_url
        global project_id
        project_id = re.findall(r"projectId=(.+?)&", current_url)[0]
        project_instance_code = re.findall(r"projectCode=(.+?)&", current_url)
        print('项目：' + str(project_instance_code[0]))

        # 项目名称
        project_name = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectName"]')
        project_name.click()
        project_name.clear()
        project_name.send_keys(str(project_id) + "测试项目")

        # 获取项目名称
        global project_name_value
        project_name_value = project_name.get_attribute('textContent')

        # 项目造价
        project_cast = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectCast"]/div[2]/input')
        project_cast.clear()
        project_cast.send_keys(str(round(random.uniform(10000000, 49999999), 2)))

        # 获取项目造价
        global project_cast_value
        project_cast_value = project_cast.get_attribute('textContent')

        # 项目类型
        project_type_location = '//*[@id="projectInfoBaseDTO.projectTypeId"]/div/div'
        project_type_options_location = '/html/body/div[2]/div/div/div/ul/li'
        SelectorUtils().selector_choose(browser, project_type_location, project_type_options_location)

        # 项目地址：省市区
        project_address_location = '//*[@id="projectInfoBaseDTO.regionNumber"]'
        province_options_location = '/html/body/div[3]/div/div/div/ul[1]'
        city_options_location = '/html/body/div[3]/div/div/div/ul[2]'
        area_options_location = '/html/body/div[3]/div/div/div/ul[3]'

        project_address = browser.find_element_by_xpath(project_address_location)
        # project_address.click()
        browser.execute_script('arguments[0].click();', project_address)

        # 选择省
        province_options_outer = browser.find_element_by_xpath(province_options_location)
        province_options = province_options_outer.find_elements_by_tag_name('li')
        province_options_sum = len(province_options)
        province_one_option = browser.find_element_by_xpath \
            (province_options_location + '/li[' + str(random.randint(1, province_options_sum)) + ']')
        browser.execute_script('arguments[0].click();', province_one_option)

        # 选择市
        city_options_outer = browser.find_element_by_xpath(city_options_location)
        city_options = city_options_outer.find_elements_by_tag_name('li')
        city_options_sum = len(city_options)
        city_one_option = browser.find_element_by_xpath \
            (city_options_location + '/li[' + str(random.randint(1, city_options_sum)) + ']')
        browser.execute_script('arguments[0].click();', city_one_option)

        # 选择区
        area_options_outer = browser.find_element_by_xpath(area_options_location)
        area_options = area_options_outer.find_elements_by_tag_name('li')
        area_options_sum = len(area_options)
        area_one_option = browser.find_element_by_xpath \
            (area_options_location + '/li[' + str(random.randint(1, area_options_sum)) + ']')
        browser.execute_script('arguments[0].click();', area_one_option)

        # 获取项目省市区
        global project_address_value
        project_address_value = project_address.get_attribute('textContent')

        # 项目详细地址
        project_address_detail = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.addressDetail"]')
        project_address_detail.clear()
        project_address_detail.send_keys(str(project_id)+ "项目详细地址")

        # 业主
        owner = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.owner"]')
        owner.clear()
        owner.send_keys(str(project_id) + "项目业主")

        # 代理公司
        agency = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.agency"]')
        agency.clear()
        agency.send_keys(str(project_id)+ "项目代理公司")

        # 资金来源
        fund_source_location = '//*[@id="projectInfoBaseDTO.fundsSourceId"]/div/div'
        fund_source_ops_location = '/html/body/div[4]/div/div/div/ul/li'
        SelectorUtils().selector_choose(browser, fund_source_location, fund_source_ops_location)

        # 商业模式
        bussiness_mode_location = '//*[@id="projectInfoBaseDTO.businessModeId"]'
        bussiness_mode_ops_location = '/html/body/div[5]/div/div/div/ul/li'
        SelectorUtils().selector_choose(browser, bussiness_mode_location, bussiness_mode_ops_location)

        # 竞争方式
        competition_mode_location = '//*[@id="projectInfoBaseDTO.competitionModeId"]/div/div'
        competition_mode_ops_location = '/html/body/div[6]/div/div/div/ul/li'
        SelectorUtils().selector_choose(browser, competition_mode_location, competition_mode_ops_location)

        # TODO：竞争方式选其他（待修改）
        competition_mode_text = browser.find_element_by_xpath(competition_mode_location).get_attribute('textContent')
        if competition_mode_text == u'其他':
            competition_mode_other = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.competitionModeOther"]')
            competition_mode_other.send_keys(str(project_id)+ "其他竞争方式")

        # 预计工期
        expected_construction_period_location = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO'
                                                                              '.expectedConstructionPeriod"]/div['
                                                                              '2]/input')
        expected_construction_period_location.clear()
        expected_construction_period_location.send_keys(random.randint(1, 10000))

        # 付款条件
        payment_condition = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.paymentCondition"]')
        payment_condition.clear()
        payment_condition.send_keys(str(project_id) + "付款条件")

        # 项目概况
        project_overview = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectOverview"]')
        project_overview.clear()
        project_overview.send_keys(str(project_id) + "项目概括")

        # # 备用金
        # reserve_fund = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.reserveFund"]/div[2]/input')
        # reserve_fund.clear()
        # reserve_fund_value = str(random.randint(100, 100000))
        # print(reserve_fund_value)
        # reserve_fund.send_keys(reserve_fund_value)
        #
        # # 备用金用途
        # reserve_fund_use = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.reserveFundUse"]')
        # reserve_fund_use.clear()
        # reserve_fund_use.send_keys(str(project_id) + "备用金用途")

    def entry_exclusive_info(self, browser):
        global project_id
        # 项目具体来源
        project_source = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectSourceDetail"]')
        project_source.clear()
        project_source.send_keys(str(project_id) + "项目具体来源")

        # 预计进入程序时间
        expected_process_time = browser.find_element_by_xpath(
            '//*[@id="projectInfoBaseDTO.expectedProgramTime"]/div/input'
        )
        # time.sleep(1)
        browser.execute_script("arguments[0].click();", expected_process_time)
        today = browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div[2]/div[3]/span/a')
        browser.execute_script("arguments[0].click();", today)

        # 竞争对手
        competitor = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.competitor"]')
        competitor.clear()
        competitor.send_keys(str(project_id) + "竞争对手")

        # 技术难度
        technical_difficulty = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.technicalDifficulty"]')
        technical_difficulty.clear()
        technical_difficulty.send_keys(str(project_id) + "技术难度")

        # 施工条件
        construction_condition = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.constructionConditions"]')
        construction_condition.clear()
        construction_condition.send_keys(str(project_id) + "施工条件")

    def self_evaluation_info(self, browser):
        global project_id
        # 自我评测-投入周期计划-标前阶段投入
        # tender_stage_input_before = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.tenderStageInputBefore"]')
        # tender_stage_input_before.clear()
        # tender_stage_input_before.send_keys(str(project_id) + "标前阶段投入")
        #
        # # # 自我评测-投入周期计划-投标阶段投入
        # # tender_stage_input = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.tenderStageInput"]')
        # # tender_stage_input.clear()
        # # tender_stage_input.send_keys(str(project_id) + "投标阶段投入")
        # #
        # # # 自我评测-投入周期计划-建设阶段投入
        # # construction_stage_input = browser.find_element_by_xpath \
        # #     ('//*[@id="projectInfoSelfevaluationDTO.constructionStageInput"]')
        # # construction_stage_input.clear()
        # # construction_stage_input.send_keys(str(project_id) + "建设阶段投入")
        #
        # # 自我评测-收入周期计划-标前阶段收入
        # tender_stage_income_before = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.tenderStageIncomeBefore"]')
        # tender_stage_income_before.clear()
        # tender_stage_income_before.send_keys(str(project_id) + "标前阶段收入")
        #
        # # 自我评测-收入周期计划-投标阶段收入
        # tender_stage_income = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.tenderStageIncome"]')
        # tender_stage_income.clear()
        # tender_stage_income.send_keys(str(project_id) + "投标阶段收入")
        #
        # # 自我评测-收入周期计划-建设阶段收入
        # construction_stage_income = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.constructionStageIncome"]')
        # construction_stage_income.clear()
        # construction_stage_income.send_keys(str(project_id) + "建设阶段收入")
        #
        # # 自我评测-拟投入资源-时间
        # expected_input_source_time = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceTime"]')
        # expected_input_source_time.clear()
        # expected_input_source_time.send_keys(str(project_id) + "拟投入资源-时间")
        #
        # # 自我评测-拟投入资源-人力
        # expected_input_source_manpower = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceManpower"]')
        # expected_input_source_manpower.clear()
        # expected_input_source_manpower.send_keys(str(project_id) + "拟投入资源-人力")
        #
        # # 自我评测-拟投入资源-证书
        # expected_input_source_cert = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceCert"]')
        # expected_input_source_cert.clear()
        # expected_input_source_cert.send_keys(str(project_id) + "拟投入资源-证书")
        #
        # # 自我评测-拟投入资源-业绩
        # expected_input_source_performance = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourcePerformance"]')
        # expected_input_source_performance.clear()
        # expected_input_source_performance.send_keys(str(project_id) + "拟投入资源-业绩")
        #
        # # 自我评测-拟投入资源-荣誉
        # expected_input_source_honor = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceHonor"]')
        # expected_input_source_honor.clear()
        # expected_input_source_honor.send_keys(str(project_id) + "拟投入资源-荣誉")
        #
        # # 自我评测-拟投入资源-资金
        # expected_input_source_fund = browser.find_element_by_xpath \
        #     ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceFund"]')
        # expected_input_source_fund.clear()
        # expected_input_source_fund.send_keys(str(project_id) + "拟投入资源-资金")
        #
        # # 自我评测-风险点-现场环境
        # risk_site_enviroment = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskSiteEnv"]')
        # risk_site_enviroment.clear()
        # risk_site_enviroment.send_keys(str(project_id) + "风险点-现场环境")
        #
        # # 自我评测-风险点-社会环境
        # risk_social_enviroment = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskSocietyEnv"]')
        # risk_social_enviroment.clear()
        # risk_social_enviroment.send_keys(str(project_id) + "风险点-社会环境")
        #
        # # 自我评测-风险点-技术风险
        # risk_technology = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskTechnology"]')
        # risk_technology.clear()
        # risk_technology.send_keys(str(project_id) + "风险点-技术风险")
        #
        # # 自我评测-风险点-质量风险
        # risk_quality = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskQuality"]')
        # risk_quality.clear()
        # risk_quality.send_keys(str(project_id) + "风险点-质量风险")
        #
        # # 自我评测-风险点-安全风险
        # risk_safety = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskSafety"]')
        # risk_safety.clear()
        # risk_safety.send_keys(str(project_id) + "风险点-安全风险")
        #
        # # 自我评测-风险点-资金风险
        # risk_fund = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskFund"]')
        # risk_fund.clear()
        # risk_fund.send_keys(str(project_id) + "风险点-资金风险")
        #
        # # 自我评测-风险点-政策风险
        # risk_policy = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskPolicy"]')
        # risk_policy.clear()
        # risk_policy.send_keys(str(project_id) + "风险点-政策风险")
        #
        # # 自我评测-风险点-政治风险
        # risk_political = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskPolitical"]')
        # risk_political.clear()
        # risk_political.send_keys(str(project_id) + "风险点-政治风险")
        #
        # # 自我评测-风险点-合作方风险
        # risk_partner = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskPartner"]')
        # risk_partner.clear()
        # risk_partner.send_keys(str(project_id) + "风险点-合作方风险")
        #
        # # 自我评测-收益-品牌
        # income_brand = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomeBrand"]')
        # income_brand.clear()
        # income_brand.send_keys(str(project_id) + "收益-品牌")
        #
        # # 自我评测-收益-队伍
        # income_team = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomeTeam"]')
        # income_team.clear()
        # income_team.send_keys(str(project_id) + "收益-队伍")
        #
        # # 自我评测-收益-荣誉
        # income_honor = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomeHonor"]')
        # income_honor.clear()
        # income_honor.send_keys(str(project_id) + "收益-荣誉")
        #
        # # 自我评测-收益-业绩
        # income_performance = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomePerformance"]')
        # income_performance.clear()
        # income_performance.send_keys(str(project_id) + "收益-业绩")
        #
        # # 自我评测-收益-利润
        # income_profit = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomeProfit"]')
        # income_profit.clear()
        # income_profit.send_keys(str(project_id) + "收益-利润")

        # 自我评测-综合评估
        comprehensive_eveluation = browser.find_element_by_xpath \
            ('//*[@id="projectInfoSelfevaluationDTO.comprehensiveEvaluation"]')
        comprehensive_eveluation.clear()
        comprehensive_eveluation.send_keys(str(project_id) + "综合评估")

    def button(self, browser):
        # 保存草稿
        save_buttuon = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div['
                                                     '3]/div/button[1]')
        save_buttuon.click()
        time.sleep(1)

        # 发起评审
        initiate_approval_button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div['
                                                                 '2]/div/div[3]/div/button[2]')
        initiate_approval_button.click()

        time.sleep(1)
        # 确认发起审批
        initiate_approval_confirm_button = browser.find_element_by_xpath('//div[@class="ant-modal-content"]/div[@class="ant-modal-footer"]//button[2]')
        browser.execute_script('arguments[0].click()', initiate_approval_confirm_button)

    def info_entry(self, browser):
        global project_id
        self.project_common_info(browser)
        self.entry_exclusive_info(browser)
        self.self_evaluation_info(browser)
        self.button(browser)
    # def info_entry(self, browser):
    #     current_url = browser.current_url
    #     global project_id
    #     project_id = re.findall(r"projectId=(.+?)&", current_url)[0]
    #     project_instance_code = re.findall(r"projectCode=(.+?)&", current_url)
    #     print '项目：' + str(project_instance_code[0])
    #
    #     # 项目名称
    #     project_name = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectName"]')
    #     project_name.click()
    #     project_name.clear()
    #     project_name.send_keys((str(project_id).encode('utf-8') + "测试项目").decode('utf-8'))
    #
    #     # 获取项目名称
    #     global project_name_value
    #     project_name_value = project_name.get_attribute('textContent')
    #
    #     # 项目造价
    #     project_cast = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectCast"]/div[2]/input')
    #     project_cast.clear()
    #     project_cast.send_keys(str(round(random.uniform(10000000, 110000000), 2)))
    #
    #     # 获取项目造价
    #     global project_cast_value
    #     project_cast_value = project_cast.get_attribute('textContent')
    #
    #     # 项目类型
    #     project_type_location = '//*[@id="projectInfoBaseDTO.projectTypeId"]/div/div'
    #     project_type_options_location = '/html/body/div[2]/div/div/div/ul/li'
    #     SelectorUtils().selector_choose(browser, project_type_location, project_type_options_location)
    #
    #     # 项目具体来源
    #     project_source = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectSourceDetail"]')
    #     project_source.clear()
    #     project_source.send_keys((str(project_id).encode('utf-8') + "项目具体来源").decode('utf-8'))
    #
    #     # 项目地址：省市区
    #     project_address_location = '//*[@id="projectInfoBaseDTO.regionNumber"]'
    #     province_options_location = '/html/body/div[3]/div/div/div/ul[1]'
    #     city_options_location = '/html/body/div[3]/div/div/div/ul[2]'
    #     area_options_location = '/html/body/div[3]/div/div/div/ul[3]'
    #
    #     project_address = browser.find_element_by_xpath(project_address_location)
    #     # project_address.click()
    #     browser.execute_script('arguments[0].click();', project_address)
    #
    #     # 选择省
    #     province_options_outer = browser.find_element_by_xpath(province_options_location)
    #     province_options = province_options_outer.find_elements_by_tag_name('li')
    #     province_options_sum = len(province_options)
    #     province_one_option = browser.find_element_by_xpath\
    #         (province_options_location + '/li[' + str(random.randint(1, province_options_sum)) + ']')
    #     province_one_option.click()
    #
    #     # 选择市
    #     city_options_outer = browser.find_element_by_xpath(city_options_location)
    #     city_options = city_options_outer.find_elements_by_tag_name('li')
    #     city_options_sum = len(city_options)
    #     city_one_option = browser.find_element_by_xpath \
    #         (city_options_location + '/li[' + str(random.randint(1, city_options_sum)) + ']')
    #     city_one_option.click()
    #
    #     # 选择区
    #     area_options_outer = browser.find_element_by_xpath(area_options_location)
    #     area_options = area_options_outer.find_elements_by_tag_name('li')
    #     area_options_sum = len(area_options)
    #     area_one_option = browser.find_element_by_xpath \
    #         (area_options_location + '/li[' + str(random.randint(1, area_options_sum)) + ']')
    #     area_one_option.click()
    #
    #     # 获取项目省市区
    #     global project_address_value
    #     project_address_value = project_address.get_attribute('textContent')
    #
    #     # 项目详细地址
    #     project_address_detail = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.addressDetail"]')
    #     project_address_detail.clear()
    #     project_address_detail.send_keys((str(project_id).encode('utf-8') + "项目详细地址").decode('utf-8'))
    #
    #     # 业主
    #     owner = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.owner"]')
    #     owner.clear()
    #     owner.send_keys((str(project_id).encode('utf-8') + "项目业主").decode('utf-8'))
    #
    #     # 代理公司
    #     agency = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.agency"]')
    #     agency.clear()
    #     agency.send_keys((str(project_id).encode('utf-8') + "项目代理公司").decode('utf-8'))
    #
    #     # 资金来源
    #     fund_source_location = '//*[@id="projectInfoBaseDTO.fundsSourceId"]/div/div'
    #     fund_source_ops_location = '/html/body/div[4]/div/div/div/ul/li'
    #     SelectorUtils().selector_choose(browser, fund_source_location, fund_source_ops_location)
    #
    #     # 商业模式
    #     bussiness_mode_location = '//*[@id="projectInfoBaseDTO.businessModeId"]'
    #     bussiness_mode_ops_location = '/html/body/div[5]/div/div/div/ul/li'
    #     SelectorUtils().selector_choose(browser, bussiness_mode_location, bussiness_mode_ops_location)
    #
    #     # 竞争方式
    #     competition_mode_location = '//*[@id="projectInfoBaseDTO.competitionModeId"]/div/div'
    #     competition_mode_ops_location = '/html/body/div[6]/div/div/div/ul/li'
    #     SelectorUtils().selector_choose(browser, competition_mode_location, competition_mode_ops_location)
    #
    #     # 竞争方式选其他
    #     competition_mode_text = browser.find_element_by_xpath(competition_mode_location).get_attribute('textContent')
    #     if competition_mode_text == u'其他':
    #         competition_mode_other = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.competitionModeOther"]')
    #         competition_mode_other.send_keys((str(project_id).encode('utf-8') + "其他竞争方式").decode('utf-8'))
    #
    #     # 预计工期
    #     expected_construction_period_location = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO'
    #                                                                           '.expectedConstructionPeriod"]/div['
    #                                                                           '2]/input')
    #     expected_construction_period_location.clear()
    #     expected_construction_period_location.send_keys(random.randint(1, 10000))
    #
    #     # 预计进入程序时间
    #     expected_process_time = browser.find_element_by_xpath(
    #         '//*[@id="projectInfoBaseDTO.expectedProgramTime"]/div/input'
    #     )
    #     # time.sleep(1)
    #     browser.execute_script("arguments[0].click();", expected_process_time)
    #     today = browser.find_element_by_xpath('/html/body/div[7]/div/div/div/div/div[2]/div[3]/span/a')
    #     browser.execute_script("arguments[0].click();", today)
    #
    #     # js去掉readonly属性
    #     # remove_readonly_js = '$(".ant-calendar-input").attr("readonly",false)'
    #     # browser.execute_script(remove_readonly_js)
    #
    #     # now_time = datetime.datetime.now()
    #     # now_date = datetime.datetime.strftime(now_time, '%Y-%m-%d')
    #     # expected_process_time.send_keys(now_date)
    #     # today = browser.find_element_by_class_name("ant-calendar-today-btn ")
    #
    #     # 竞争对手
    #     competitor = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.competitor"]')
    #     competitor.clear()
    #     competitor.send_keys((str(project_id).encode('utf-8') + "竞争对手").decode('utf-8'))
    #
    #     # 技术难度
    #     technical_difficulty = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.technicalDifficulty"]')
    #     technical_difficulty.clear()
    #     technical_difficulty.send_keys((str(project_id).encode('utf-8') + "技术难度").decode('utf-8'))
    #
    #     # 付款条件
    #     payment_condition = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.paymentCondition"]')
    #     payment_condition.clear()
    #     payment_condition.send_keys((str(project_id).encode('utf-8') + "付款条件").decode('utf-8'))
    #
    #     # 施工条件
    #     construction_condition = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.constructionConditions"]')
    #     construction_condition.clear()
    #     construction_condition.send_keys((str(project_id).encode('utf-8') + "施工条件").decode('utf-8'))
    #
    #     # 项目概况
    #     project_overview = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.projectOverview"]')
    #     project_overview.clear()
    #     project_overview.send_keys((str(project_id).encode('utf-8') + "项目概括").decode('utf-8'))
    #
    #     # 备用金
    #     reserve_fund = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.reserveFund"]/div[2]/input')
    #     reserve_fund.clear()
    #     reserve_fund_value = str(random.randint(100, 100000))
    #     print reserve_fund_value
    #     reserve_fund.send_keys(reserve_fund_value)
    #
    #     # 备用金用途
    #     reserve_fund_use = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.reserveFundUse"]')
    #     reserve_fund_use.clear()
    #     reserve_fund_use.send_keys((str(project_id).encode('utf-8') + "备用金用途").decode('utf-8'))
    #
    #     # 自我评测-投入周期计划-标前阶段投入
    #     tender_stage_input_before = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.tenderStageInputBefore"]')
    #     tender_stage_input_before.clear()
    #     tender_stage_input_before.send_keys((str(project_id).encode('utf-8') + "标前阶段投入").decode('utf-8'))
    #
    #     # 自我评测-投入周期计划-投标阶段投入
    #     tender_stage_input = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.tenderStageInput"]')
    #     tender_stage_input.clear()
    #     tender_stage_input.send_keys((str(project_id).encode('utf-8') + "投标阶段投入").decode('utf-8'))
    #
    #     # 自我评测-投入周期计划-建设阶段投入
    #     construction_stage_input = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.constructionStageInput"]')
    #     construction_stage_input.clear()
    #     construction_stage_input.send_keys((str(project_id).encode('utf-8') + "建设阶段投入").decode('utf-8'))
    #
    #     # 自我评测-收入周期计划-标前阶段收入
    #     tender_stage_income_before = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.tenderStageIncomeBefore"]')
    #     tender_stage_income_before.clear()
    #     tender_stage_income_before.send_keys((str(project_id).encode('utf-8') + "标前阶段收入").decode('utf-8'))
    #
    #     # 自我评测-收入周期计划-投标阶段收入
    #     tender_stage_income = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.tenderStageIncome"]')
    #     tender_stage_income.clear()
    #     tender_stage_income.send_keys((str(project_id).encode('utf-8') + "投标阶段收入").decode('utf-8'))
    #
    #     # 自我评测-收入周期计划-建设阶段收入
    #     construction_stage_income = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.constructionStageIncome"]')
    #     construction_stage_income.clear()
    #     construction_stage_income.send_keys((str(project_id).encode('utf-8') + "建设阶段收入").decode('utf-8'))
    #
    #     # 自我评测-拟投入资源-时间
    #     expected_input_source_time = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceTime"]')
    #     expected_input_source_time.clear()
    #     expected_input_source_time.send_keys((str(project_id).encode('utf-8') + "拟投入资源-时间").decode('utf-8'))
    #
    #     # 自我评测-拟投入资源-人力
    #     expected_input_source_manpower = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceManpower"]')
    #     expected_input_source_manpower.clear()
    #     expected_input_source_manpower.send_keys((str(project_id).encode('utf-8') + "拟投入资源-人力").decode('utf-8'))
    #
    #     # 自我评测-拟投入资源-证书
    #     expected_input_source_cert = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceCert"]')
    #     expected_input_source_cert.clear()
    #     expected_input_source_cert.send_keys((str(project_id).encode('utf-8') + "拟投入资源-证书").decode('utf-8'))
    #
    #     # 自我评测-拟投入资源-业绩
    #     expected_input_source_performance = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourcePerformance"]')
    #     expected_input_source_performance.clear()
    #     expected_input_source_performance.send_keys((str(project_id).encode('utf-8') + "拟投入资源-业绩").decode('utf-8'))
    #
    #     # 自我评测-拟投入资源-荣誉
    #     expected_input_source_honor = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceHonor"]')
    #     expected_input_source_honor.clear()
    #     expected_input_source_honor.send_keys((str(project_id).encode('utf-8') + "拟投入资源-荣誉").decode('utf-8'))
    #
    #     # 自我评测-拟投入资源-资金
    #     expected_input_source_fund = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.expectedInputSourceFund"]')
    #     expected_input_source_fund.clear()
    #     expected_input_source_fund.send_keys((str(project_id).encode('utf-8') + "拟投入资源-资金").decode('utf-8'))
    #
    #     # 自我评测-风险点-现场环境
    #     risk_site_enviroment = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskSiteEnv"]')
    #     risk_site_enviroment.clear()
    #     risk_site_enviroment.send_keys((str(project_id).encode('utf-8') + "风险点-现场环境").decode('utf-8'))
    #
    #     # 自我评测-风险点-社会环境
    #     risk_social_enviroment = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskSocietyEnv"]')
    #     risk_social_enviroment.clear()
    #     risk_social_enviroment.send_keys((str(project_id).encode('utf-8') + "风险点-社会环境").decode('utf-8'))
    #
    #     # 自我评测-风险点-技术风险
    #     risk_technology = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskTechnology"]')
    #     risk_technology.clear()
    #     risk_technology.send_keys((str(project_id).encode('utf-8') + "风险点-技术风险").decode('utf-8'))
    #
    #     # 自我评测-风险点-质量风险
    #     risk_quality = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskQuality"]')
    #     risk_quality.clear()
    #     risk_quality.send_keys((str(project_id).encode('utf-8') + "风险点-质量风险").decode('utf-8'))
    #
    #     # 自我评测-风险点-安全风险
    #     risk_safety = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskSafety"]')
    #     risk_safety.clear()
    #     risk_safety.send_keys((str(project_id).encode('utf-8') + "风险点-安全风险").decode('utf-8'))
    #
    #     # 自我评测-风险点-资金风险
    #     risk_fund = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskFund"]')
    #     risk_fund.clear()
    #     risk_fund.send_keys((str(project_id).encode('utf-8') + "风险点-资金风险").decode('utf-8'))
    #
    #     # 自我评测-风险点-政策风险
    #     risk_policy = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskPolicy"]')
    #     risk_policy.clear()
    #     risk_policy.send_keys((str(project_id).encode('utf-8') + "风险点-政策风险").decode('utf-8'))
    #
    #     # 自我评测-风险点-政治风险
    #     risk_political = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskPolitical"]')
    #     risk_political.clear()
    #     risk_political.send_keys((str(project_id).encode('utf-8') + "风险点-政治风险").decode('utf-8'))
    #
    #     # 自我评测-风险点-合作方风险
    #     risk_partner = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.riskPartner"]')
    #     risk_partner.clear()
    #     risk_partner.send_keys((str(project_id).encode('utf-8') + "风险点-合作方风险").decode('utf-8'))
    #
    #     # 自我评测-收益-品牌
    #     income_brand = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomeBrand"]')
    #     income_brand.clear()
    #     income_brand.send_keys((str(project_id).encode('utf-8') + "收益-品牌").decode('utf-8'))
    #
    #     # 自我评测-收益-队伍
    #     income_team = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomeTeam"]')
    #     income_team.clear()
    #     income_team.send_keys((str(project_id).encode('utf-8') + "收益-队伍").decode('utf-8'))
    #
    #     # 自我评测-收益-荣誉
    #     income_honor = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomeHonor"]')
    #     income_honor.clear()
    #     income_honor.send_keys((str(project_id).encode('utf-8') + "收益-荣誉").decode('utf-8'))
    #
    #     # 自我评测-收益-业绩
    #     income_performance = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomePerformance"]')
    #     income_performance.clear()
    #     income_performance.send_keys((str(project_id).encode('utf-8') + "收益-业绩").decode('utf-8'))
    #
    #     # 自我评测-收益-利润
    #     income_profit = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.incomeProfit"]')
    #     income_profit.clear()
    #     income_profit.send_keys((str(project_id).encode('utf-8') + "收益-利润").decode('utf-8'))
    #
    #     # 自我评测-综合评估
    #     comprehensive_eveluation = browser.find_element_by_xpath\
    #         ('//*[@id="projectInfoSelfevaluationDTO.comprehensiveEvaluation"]')
    #     comprehensive_eveluation.clear()
    #     comprehensive_eveluation.send_keys((str(project_id).encode('utf-8') + "综合评估").decode('utf-8'))
    #
    #     # 保存草稿
    #     save_buttuon = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div['
    #                                                  '3]/div/button[1]')
    #     save_buttuon.click()
    #
    #     # 发起评审
    #     initiate_approval_button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div['
    #                                                              '2]/div/div[3]/div/button[2]')
    #     initiate_approval_button.click()
    #
    #     # 确认发起审批
    #     initiate_approval_confirm_button = browser.find_element_by_css_selector('html body div div div.ant-modal-wrap '
    #                                                                             'div.ant-modal div.ant-modal-content '
    #                                                                             'div.ant-modal-footer div '
    #                                                                             'button.ant-btn.ant-btn-primary')
    #     browser.execute_script('arguments[0].click()', initiate_approval_confirm_button)

    def get_proiect_id(self):
        print('项目ID：' + str(project_id))
        return project_id

    def get_project_name(self):
        print('项目名称' + project_name_value)
        return project_name_value

    def get_project_cast(self):
        print('项目造价' + str(project_cast_value))
        return project_cast_value

    def get_project_address(self):
        print('项目地址' + project_address_value)
        return project_address_value


if __name__ == "__main__":
    # print (str(47).encode('utf-8') + "测试项目").decode('utf-8')
    print(round(random.uniform(10000000, 50000000), 2))
