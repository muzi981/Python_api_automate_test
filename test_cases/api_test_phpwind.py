'''
PHPwind首页登录接口测试用例
'''
import re
import requests


class Test_PHPwind:
    # 定义类变量
    url = "http://47.107.116.139"
    csrf_token = ''  # 获取csrf_token值
    sess = requests.session()  # 创建requests.session()方法，用来后面session.request()调用接口，从而直接放弃原有requests.get()

    # PHPwind首页获取html标签中隐藏的csrf_token值；
    def test_phpwind_home_page(self):
        url = "http://47.107.116.139/phpwind"
        # res_get = requests.get(url=url)
        # text = res_get.text
        # print(text)
        text = Test_PHPwind.sess.request('get', url=url).text
        # 通过正则表达式re.search来获取token值，并将值保存到类变量csrf_token中
        Test_PHPwind.csrf_token = re.search('name="csrf_token" value="(.*?)"', text).group(1)
        print(Test_PHPwind.csrf_token)

    # PHPwind登录接口
    def test_phpwind_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        # 请求头
        headers = {
            "Accept": "application/json, text/javascript, /; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        # 请求参数json
        data = {
            "username": "baili",
            "password": "baili123",
            "csrf_token": Test_PHPwind.csrf_token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        # json =  requests.post(url=url, data=data, headers=headers).json()
        # 这样调用后最终失败，原因是requests.request()和session.request()的区别：
        # 前者每个请求都是独立的，后者会自动关了所有请求的cookie信息。
        json = Test_PHPwind.sess.request('post', url=url, data=data, headers=headers).json()
        print(json)


if __name__ == '__main__':
    # 测试获取html中隐藏csrf_token值
    Test_PHPwind.test_phpwind_home_page()
    # 测试登录接口
    Test_PHPwind.test_phpwind_login()
