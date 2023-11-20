from test_cases import api_test_weixin

if __name__ == '__main__':
    api_test_weixin.TestApi().test_weixin_cookie()
    api_test_weixin.TestApi().test_weixin_tag()
    api_test_weixin.TestApi().test_weixin_edit_tag()