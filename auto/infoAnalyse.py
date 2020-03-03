# coding=utf-8

import time
from infoEntry import InfoEntry


class InfoAnalyse(object):
    def analyse_exclusive(self, browser):
        # 招标文件上传

        # 开标时间
        tender_start_time = browser.find_element_by_xpath('')

        # 现场踏勘时间

        # 招标要求
        # 资信标分数占比

        # 商务标分数占比

        # 技术标分数占比


    def info_analyse(self, browser):
        comomon_info = InfoEntry(browser)
        comomon_info.project_common_info(browser)
        self.analyse_exclusive(browser)

        # TODO: 根据项目来源确定是否调用 comomon_info.self_evaluation_info(browser)

        comomon_info.button(browser)