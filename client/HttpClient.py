# coding=utf-8import requestsimport jsonclass HttpClient(object):    """    Something TODO:    """    """    1。addr 是什么？    2。path 是什么？    3。这两个词都太模糊：是不是应该改成：host，uri    4。这种组装结果返回的，尽量使用 build，create等词汇    5。get 用于获取已存在的东西时使用，比如：getOneUser    6。@classmethod 了解一下    7。static 方法了解下    8。刚刚那里是屏蔽了警，没把握的话不要屏蔽    9。从本地恢复代码    """    def get_url(self, addr, path):        return ''.join([addr, path])    def dopost(self, addr, path, data, headers):        result = requests.post(self.get_url(addr, path), data, headers)        return result    def doget(self, url, data, headers):        result = requests.get(url, data, headers)        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)    def dodelete(self, url, data, headers):        result = requests.get(url, data, headers) # 这个参数可能是可有可无 按住command + 鼠标左：**kwargs 这个是可变参数    def __run_main(self, method, url=None, data=None, headers=None):        # 这个其实只是一个测试代码，所以它不是对外提供的完成某一功能的方法，所以是私有的，避免引入此类的 python file 误执行        # 这样写才健壮，必要的时候加上异常处理        if method is None or url is None or headers is None:            return None        result = None        if method == 'post':            result = self.dopost(url, data, headers)        elif method == 'get':            result = self.doget(url, data, headers)        elif method == 'delete':            result = self.dodelete(url, data, headers)        else:            print("错误")        return resultif __name__ == "__main__":    # 在上面所有接口中除特殊情况应该返回相同数据结构 要么全是json 要么全不是    # 以后测试代码这样写    # 学习一下 py 中 private public protected，该什么时候使用这三种访问限定符    client = HttpClient()    client.__run_main()