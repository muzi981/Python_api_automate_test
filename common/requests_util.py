'''
# 统一请求的封装
'''
import requests

class RequestsUtil:

    see = requests.session()
    # 统一封装请求
    def unify_api_requests(self,**kwargs):
        # 请求方式
        res = RequestsUtil.see.request(**kwargs)
        # 打印请求结果
        print('\n用例测试结果：', res.json())
        return res