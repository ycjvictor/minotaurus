# coding=utf-8import reclass RegexUtils(object):    # 以后代码记者 字符集 和导包隔开一个空行 导包和代码或者 class 隔开两个空行    # 系统和第三方/官方提供的 package 放到自定义 package 之上    # 以后你可能会大量使用正则表达式，要去学着写牛逼的正则表达式    # 下边这三个是我觉得写的不错的，够你用到退休了这三个    __re_url = "(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]"    __re_ip = "(2(5[0-5]{1}|[0-4]\\d{1})|[0-1]?\\d{1,2})(\\.(2(5[0-5]{1}|[0-4]\\d{1})|[0-1]?\\d{1,2})){3}"    __re_time = "[1-9]\\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])\\s+(20|21|22|23|[0-1]\\d):[0-5]\\d:[0-5]\\d"    def find_url(self, src):        return re.findall(self.__re_url, src)    def find_ip(self, src):        return re.findall(self.__re_ip, src)    def find_time(self, src):        return re.findall(self.__re_time, src)