# coding=utf-8import requestsimport datetimeimport jsonclass HttpClient(object):    def build_url(self, host, uri):        return ''.join([host, uri])    def dopost(self, host, uri, data, headers):        url = self.build_url(host, uri)        return requests.post(url, data=json.dumps(data), headers=headers)    def doget(self, host, uri, data, headers):        url = self.build_url(host, uri)        return requests.get(url, data=data, headers=headers)    def dodelete(self, host, uri, data, headers):        url = self.build_url(host, uri)        return requests.delete(url, data=json.dumps(data), headers=headers)    def doput(self, host, uri, data, headers):        url = self.build_url(host, uri)        return requests.put(url, data=json.dumps(data), headers=headers)    # def run_main(self, method, host, uri, data, headers):    #     # 这个其实只是一个测试代码，所以它不是对外提供的完成某一功能的方法，所以是私有的，避免引入此类的 python file 误执行    #     # 这样写才健壮，必要的时候加上异常处理    #     if method is None or host is None or uri is None or headers is None:    #         return None    #     val = None    #     if method == 'post':    #         val = self.dopost(host, uri, data, headers)    #     elif method == 'get':    #         val = self.doget(host, uri, data, headers)    #     elif method == 'delete':    #         print 'TODO: When method is delete'    #     elif method == 'put':    #         print 'TODO: When method is put'    #     else:    #         print("请求方法错误")    #     return valif __name__ == "__main__":    # 在上面所有接口中除特殊情况应该返回相同数据结构 要么全是json 要么全不是    # 学习一下 py 中 private public protected，该什么时候使用这三种访问限定符    client = HttpClient()    now_time = datetime.datetime.now()    headers_target = {        "reqtme":datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S'),        "Content-Type":"application/json;charset=UTF-8"    }    # postMethod = 'post'    host_target = 'http://47.96.183.143:9091'    loginUri = '/api/ums/login/signin'    loginData = {        "account": "ces001",        "password": "123456"    }    # getMethod = 'get'    logoutUri = '/api/ums/login/signout/'    sealShapeDelUri = '/api/office/seal/delete'    sealShapeDelData = {        "id": 58,        "type": 2    }    sealConfigUri = 'api/office/seal/config'    sealConfigData = {        "sealName": "5",        "type": 2,        "adscription": "2",        "id": 55    }    url_target = client.build_url(host_target, loginUri)    loginResult = client.dopost(host_target, loginUri, loginData, headers_target)    logoutResult = client.doget(host_target, logoutUri + '2', None, headers_target)    sealShapeDelResult = client.dodelete(host_target, sealShapeDelUri, sealShapeDelData, headers_target)    sealConfigResult = client.doput(host_target, sealShapeDelUri, sealConfigData, headers_target)    print(loginResult.headers)    print(logoutResult.headers)    print(sealShapeDelResult.headers)    print(sealShapeDelResult.headers)