# coding=utf-8import requestsimport jsonclass HttpClient(object):    """    Something TODO:    """    def dopost(self, url, data, headers):        result = requests.post(url, data, headers)        return result    def doget(self, url, data, headers):        result = requests.get(url, data, headers)        # res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)    # def run_main(self, method, url=None, data=None, headers=None):    #     result = None    #     if method == 'post':    #         result = self.send_post(url, data, headers)    #     elif method == 'get':    #         result = self.send_get(url, data, headers)    #     else:    #         print("错误")    #     return result