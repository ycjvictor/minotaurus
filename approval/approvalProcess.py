# coding=utf-8

import time
from selenium import webdriver
from approval import approval
from auto.login import Login
from auto.listQuery import ListQuery
from auto.infoEntry import InfoEntry


class ApprovalProcess(object):

    def info_entry_approval(self):
        # 获取项目信息
        project_info = InfoEntry()
        project_id = project_info.get_proiect_id()
        project_name = project_info.get_project_name()
        project_cast = project_info.get_project_cast()
        project_address = project_info.get_project_address()
        project_process = '信息评审'

        account_dic = {'ces008': '123456', 'ces015': '123456'}
        account_li = ['ces008', 'ces015', 'ces005', 'liuyang']

        if u'浙江省衢州市' in project_address:
            account_dic['jiangjiangao'] = '123456'
            account_li.insert(1, 'jiangjinagao')
        if project_cast > 50000000:
            account_dic['ces005'] = '123456'
            if project_cast > 1000000000:
                account_dic['liuyang'] = '123456'
        print(account_dic)



        browser = webdriver.Chrome()
        for i in range(0, len(account_dic)-1):
            account = account_li[0]
            pasaword = account_dic[account]

            login = Login()
            login.login_without_qr(browser, account, pasaword)
            time.sleep(2)
            # 查询审批通知
            ListQuery().notice_list_query(browser, project_name, project_process)

            # 审批操作
            approval_opinion = account + '审批:' + project_name + project_process

            approval = approval()
            approval.approval(browser, 1, approval_opinion)

            # # TODO: 信息录入特殊审批
            # if i == len(account_dic)-1:
            #     pass

            approval.approval_submit_button(browser)
            time.sleep(1)

            login.logout(browser)

if __name__ == "__main":
    ApprovalProcess().info_entry_approval()
