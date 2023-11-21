'''
# 微信接口测试用例
'''
import jsonpath
from common.requests_util import RequestsUtil
from common.db import Db

class Test_Weixin:
    # 创建类变量
    weixin = 'https://api.weixin.qq.com'         # 测试url
    appid = 'wx6dc7e0c9a47ec89d'                 # weixin appID值
    secret = '79020ddd6bf173ee4d0223266f9f67b7'  # weixin appsecret值
    weixin_user = 'VAJ_木子'                      # 微信用户名
    openid = Db().mysql_conn()                   # 数据库中获取用户对应的openid
    Token = ''  # weixin鉴权码
    id = ''  # weixin用户标签id

    # 获取微信鉴权码access_token信息接口
    # get请求
    def test_weixin_cookie(self):
        url = Test_Weixin.weixin + "/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": Test_Weixin.appid,
            "secret": Test_Weixin.secret
        }
        # 发送请求 get
        res_get = RequestsUtil().unify_api_requests(method='get', url=url, params=params)
        # 使用JsonPath提取token值
        Test_Weixin.Token = jsonpath.jsonpath(res_get.json(), "$.[access_token]")
        # text = res_get.text  # 返回字符串形式结果
        # json = res_get.json()  # 返回JSON格式结果，字典形式结果
        # print("\n测试获取weixin_cookie值结果：")
        # print("text格式结果：", text)
        # print("JSON格式结果：", json)
        #
        # # 使用正则表达式提取token值
        # result = re.search('access_token":"(.*?)"', text)
        # Test_Weixin.Token = result.group(1)
        # print(Test_Weixin.Token)
        # # 提取json格式结果中token值 方法一：
        # Test_Weixin.Token = json["access_token"]
        # print(Test_Weixin.Token)
        # # 使用JsonPath提取token值  方法二：
        # Test_Weixin.Token = jsonpath.jsonpath(json, "$.[access_token]")
        # print(Test_Weixin.Token[0])

    # 查询用户标签信息接口
    # get请求
    def test_weixin_tag(self):
        url = Test_Weixin.weixin + "/cgi-bin/tags/get"
        params = {
            "access_token": Test_Weixin.Token
        }
        # 发送请求 get
        res_get = RequestsUtil().unify_api_requests(method='get', url=url, params=params)
        # 结果为json
        json = res_get.json()
        # 提取标签信息中的id值存到类变量中
        Test_Weixin.id = json["tags"][1]['id']

    # 编辑用户标签信息接口
    # post请求
    def test_weixin_edit_tag(self):
        url = Test_Weixin.weixin + "/cgi-bin/tags/update"
        params = {
            "access_token": Test_Weixin.Token
        }
        json = {
            "tag": {
                "id": Test_Weixin.id,
                "name": "木子132"
            }
        }
        RequestsUtil().unify_api_requests(method='post', url=url, params=params, json=json)

    # weixin文件上传接口测试
    # post请求
    def test_weixin_files(self):
        url = Test_Weixin.weixin + "/cgi-bin/media/uploadimg"
        params = {
            "access_token": Test_Weixin.Token
        }
        files = {
            "media": open("/Users/Muzi/Desktop/Code_demo/API/Python/api_test/Python_api_automate_test/img/1.jpg", 'rb')  # 文件上传需要将文件转成二进制进行上传
        }
        RequestsUtil().unify_api_requests(method='post', url=url, params=params, files=files)


    # 查询自定义菜单接口
    def test_weixin_menu(self):
        url = Test_Weixin.weixin + '/cgi-bin/get_current_selfmenu_info'
        params = {
            "access_token": Test_Weixin.Token
        }
        RequestsUtil().unify_api_requests(method='get', url=url, params=params)

    # 个性化菜单接口创建
    # def test_weixin_Personalized_menu(self):
    #     url = Test_Weixin.weixin + '/cgi-bin/menu/addconditional'
    #     params = {
    #         "access_token": Test_Weixin.Token
    #     }
    #     json = {
    #         "button": [
    #             {
    #                 "type": "view",
    #                 "name": "muzi",
    #                 "url": "https://www.bai.com"
    #             }
    #         ],
    #         "matchrule": {
    #             "tag_id": Test_Weixin.id,
    #             "client_platform_type": "",
    #         }
    #     }
    #     RequestsUtil().unify_api_requests(method='post', url=url, params=params, json=json)

    # 个性化菜单接口查询 获取自定义菜单配置
    def test_weixin_get_Personalized_menu(self):
        url = Test_Weixin.weixin + '/cgi-bin/menu/get'
        params = {
            "access_token": Test_Weixin.Token
        }
        RequestsUtil().unify_api_requests(method='get', url=url, params=params)


    # 微信客服消息模块
    # 添加客服账号
    def test_weixin_add_Customer_service(self):
        url = Test_Weixin.weixin + '/customservice/kfaccount/add'
        params = {
            "access_token" : Test_Weixin.Token
        }
        json = {
            "kf_account": "test1@test",
            "nickname": "客服1",
            "password": "pswmd1"
        }
        RequestsUtil().unify_api_requests(method='post', url=url, params=params, json=json)

    # 修改客服账号
    def test_weixin_edit_Customer_service(self):
        url = Test_Weixin.weixin + '/customservice/kfaccount/update'
        params = {
            "access_token": Test_Weixin.Token
        }
        json = {
            "kf_account": "test1@test1",
            "nickname": "客服1",
            "password": "pswmd1"
        }
        RequestsUtil().unify_api_requests(method='post', url=url, params=params, json=json)

    # 删除客服账号
    def test_weixin_delete_Customer_service(self):
        url = Test_Weixin.weixin + '/customservice/kfaccount/del'
        params = {
            "access_token": Test_Weixin.Token
        }
        json = {
            "kf_account": "test1@test2"
        }
        RequestsUtil().unify_api_requests(method='post', url=url, params=params, json=json)

    # 设置客服账号的头像


    # 获取所有客服账号
    def test_weixin_inquire_Customer_service(self):
        url = Test_Weixin.weixin + '/cgi-bin/customservice/getkflist'
        params = {
            "access_token": Test_Weixin.Token
        }
        RequestsUtil().unify_api_requests(method='get', url=url, params=params)


    # 客服接口 - 发消息
    # 接口发送文本信息
    def test_weixin_text_Send_message(self):
        url = Test_Weixin.weixin + '/cgi-bin/message/custom/send'
        params = {
            "access_token": Test_Weixin.Token
        }
        json = {
            "touser": "OPENID",
            "msgtype": "text",
            "text":
                {
                    "content": "Hello World"
                }
        }
        RequestsUtil().unify_api_requests(method='post', url=url, params=params, json=json)
