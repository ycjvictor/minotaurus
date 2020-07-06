# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from util.SelectorUtils import SelectorUtils
from util.FileuploadUtils import FileuploadUtils
from infoEntry import InfoEntry



class InfoAnalyse(object):
    def analyse_exclusive(self, browser):
        # 招标文件上传
        tender_document_upload = browser.find_element_by_xpath('//div[@id="fileList"]//button')
        tender_document_upload.click()
        time.sleep(2)

        FileuploadUtils.upload_file(r'd:\1592200059206_6.19溧阳.pdf')

        # 开标时间
        tender_start_time = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.tenderStartTime"]//input')
        browser.execute_script("arguments[0].click();", tender_start_time)
        now_time = browser.find_element_by_xpath('//*[@class="ant-calendar-date-panel"]/div[@class="ant-calendar-footer ant-calendar-footer-show-ok"]//a')
        browser.execute_script("arguments[0].click();", now_time)

        # 现场踏勘时间
        site_survey_time = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.explorationSurveyTime"]/div/input')
        browser.execute_script("arguments[0].click();", site_survey_time)
        today = browser.find_element_by_xpath('//*[@class="ant-calendar-date-panel"]/div[@class="ant-calendar-footer"]//a')
        browser.execute_script("arguments[0].click();", today)

        # 招标要求
        # # 资信标分数占比
        # credit_mark_percentage = browser.find_element_by_xpath('//*[@id="projectTenderClaimDTO.tenderCredit"]/div[2]/input')
        # credit_mark_percentage.send_keys('10%')
        #
        # # 商务标分数占比
        # credit_mark_percentage = browser.find_element_by_xpath('//*[@id="projectTenderClaimDTO.tenderBusiness"]/div[2]/input')
        # credit_mark_percentage.send_keys('20%')
        #
        # # 技术标分数占比
        # credit_mark_percentage = browser.find_element_by_xpath('//*[@id="projectTenderClaimDTO.tenderTechnology"]/div[2]/input')
        # credit_mark_percentage.send_keys('30%')
        #
        # # 需要自制的标书
        # self_made_tenders = browser.find_elements_by_xpath('//*[@id="tenderType"]/label[1]/span/input')
        # self_made_tenders.click()

        # 是否法人出场
        legal_person_appearance = browser.find_element_by_xpath('//*[@id="projectTenderClaimDTO.needLegalPerson"]/label[2]/span[1]/input')
        legal_person_appearance.send_keys(Keys.SPACE)
        legal_person_appearance.click()

        # 是否建筑师出场
        architect_appearance = browser.find_element_by_xpath('//*[@id="projectTenderClaimDTO.needConstructor"]/label[1]/span[1]/input')
        architect_appearance.send_keys(Keys.SPACE)
        architect_appearance.click()

        # 建筑师要求
        architect_requirements_location = '//*[@id="projectTenderClaimDTO.constructorClaimId"]/div/div/div'
        architect_requirements_options_location = '/html/body/div[10]/div/div/div/ul/li'
        SelectorUtils().selector_choose(browser, architect_requirements_location, architect_requirements_options_location)
        time.sleep(1)

        architect_name = browser.find_element_by_id('projectTenderClaimDTO.constructorName')
        architect_name.send_keys('曹建民')

        # 资质要求
        qualification_requirements_location = '//*[@id="projectTenderClaimDTO.qualificationId"]'
        qualification_requirements_options_location = '/html/body/div[11]/div/div/div/ul/li'
        SelectorUtils().selector_choose(browser, qualification_requirements_location, qualification_requirements_options_location)
        browser.find_element_by_xpath(qualification_requirements_location).click()

        # 保证金缴纳方式
        browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/label[3]/span[2]').click()
        margin_payment_location = '//*[@id="projectMarginDTO.marginPaymentType"]'
        margin_payment_options_location = '/html/body/div[12]/div/div/div/ul/li[1]'
        SelectorUtils().selector_choose(browser, margin_payment_location, margin_payment_options_location)
        time.sleep(1)

        # 保证金金额
        margin_amount = browser.find_element_by_xpath('//*[@id="projectMarginDTO.marginAmount"]/div[2]/input')
        margin_amount.send_keys('80000000')

        # 保证金缴纳截止时间
        browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div/label[3]/span[1] ')
        margin_payment_deadline = browser.find_element_by_xpath('//*[@id="projectMarginDTO.marginPaymentEndTime"]/div/input')
        browser.execute_script("arguments[0].click();", margin_payment_deadline)
        today = browser.find_element_by_xpath('/html/body/div[13]/div/div/div/div/div[2]/div[3]/span/a')
        browser.execute_script("arguments[0].click();", today)

        # 保证金开户行
        margin_deposit_bank = browser.find_element_by_xpath('//*[@id="projectMarginDTO.marginBank"]')
        margin_deposit_bank.send_keys('常州市公共资源交易中心溧阳分中心')
        # 保证金户名
        margin_account_name = browser.find_element_by_xpath('//*[@id="projectMarginDTO.marginAccountName"]')
        margin_account_name.send_keys('江苏江南农村商业银行股份有限公司溧阳市溧城支行')
        # 保证金账号
        margin_account = browser.find_element_by_xpath('//*[@id="projectMarginDTO.marginAccount"]')
        margin_account.send_keys('01302018201199050471')

        # 报名方式
        registration_method_location = '//*[@id="projectInfoBaseDTO.signupModel"]'
        registration_method_options_location = '/html/body/div[14]/div/div/div/ul/li[1]'
        SelectorUtils().selector_choose(browser, registration_method_location, registration_method_options_location)

        # 报名时间
        registration_time = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.signupTime"]//input')
        browser.execute_script("arguments[0].click();", registration_time)
        today = browser.find_element_by_xpath('/html/body/div[15]/div/div/div/div/div[2]/div[3]/span/a')
        browser.execute_script("arguments[0].click();", today)

        # 报名地址
        registration_address = browser.find_element_by_xpath('//*[@id="projectInfoBaseDTO.signupAddress"]')
        registration_address.send_keys('http://60.191.53.122:81/TPBidder/login.aspx?ReturnUrl=%2fTPBidder')

        # 经营预算分析
        # 资质使用费-预计收入
        royalty_income = browser.find_element_by_xpath('//*[@id="announcement8"]/div[2]/div/div/form/table/tbody/tr[1]/td[2]/div/div[2]/input')
        royalty_income.send_keys('5000')
        # 资质使用费-预计支出
        royalty_income = browser.find_element_by_xpath('//*[@id="announcement8"]/div[2]/div/div/form/table/tbody/tr[1]/td[3]/div/div[2]/input')
        royalty_income.send_keys('5000')
        # 资质使用费-备注
        royalty_income = browser.find_element_by_xpath('//*[@id="announcement8"]/div[2]/div/div/form/table/tbody/tr[1]/td[4]/input')
        royalty_income.send_keys('无')

        # # 综合评估
        # comprehensive_assessment = browser.find_element_by_xpath('//*[@id="projectInfoSelfevaluationDTO.comprehensiveEvaluation"]')
        # comprehensive_assessment.send_keys('0')




    def info_analyse(self, browser):
        comomon_info = InfoEntry()
        comomon_info.project_common_info(browser)
        self.analyse_exclusive(browser)
        comomon_info.self_evaluation_info(browser)

        # TODO: 根据项目来源确定是否调用 comomon_info.self_evaluation_info(browser)

        comomon_info.button(browser)