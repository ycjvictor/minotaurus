# coding=utf-8import timefrom selenium import webdriverfrom auto.AutoTester import AutoTesterif __name__ == "__main__":    options = webdriver.ChromeOptions()    options.debugger_address = "127.0.0.1:9222"    browser = webdriver.Chrome(options=options)    # browser = webdriver.Chrome()    url = "http://47.96.183.143/#/login"    acctountId = "account"    passwordId = "password"    submit = "ant-btn-lg"    manager_account = "admin"    manager_password = "111111"    browser.delete_all_cookies()    auto_tester = AutoTester()    auto_tester.auto_tester(url, browser, acctountId, passwordId, submit, manager_account, manager_account, 1)