# coding=utf-8import reclass TagUtils(object):    # 如果还不是很清楚自己要成成那些内容，先这样标记起来    # 捋顺了在写不容易犯错，也会减少返工的情况    # 想好每一个函数的入参是啥，出参应该是啥，不要随便想想就写    def findtagbyclass(self, src, style):        # TODO: 通过 class 获取标签        return None    def findtagbyid(self, src, id):        # TODO: 通过 id 获取标签        return None    def findtagbyreg(self, src, reg):        return re.findall(src, reg)if __name__ == '__main__':    print("黄巧莹是猪")