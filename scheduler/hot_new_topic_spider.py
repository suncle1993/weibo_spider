#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 4/3/18 2:08 PM
@author: Chen Liang
@function: 爬取weibo热门话题（需要处理登录）
"""


from spider.base_spider import BaseSpider
from login.simulate_login import WeiboSeleniumLogin
import re


class HotNewTopicSpider(BaseSpider):
    """爬取weibo热门话题（需要处理登录）：需要获取title, url, 阅读数, 讨论数, 粉丝数"""
    def __init__(self, cookies, user_id):
        self._cookie_dict = {}
        assert isinstance(cookies, list), "argument type error"
        assert isinstance(user_id, int), "argument type error"
        for cookie in cookies:
            if 'name' in cookie and 'value' in cookie:
                self._cookie_dict[cookie['name']] = cookie['value']
        self._user_id = user_id
        self._html = self.get_html_content('https://weibo.com/u/{}/home'.format(self._user_id), self._cookie_dict)

    def get_topic_list(self):
        """获取热门话题列表"""
        topic_list = []
        pattern = r'<span class=\\"total S_txt2\\" title=\\"阅读量\\">(.*?)<.*?href=\\"\\/\\/weibo.com\\/p\\/(.*?from=' \
                  r'trendtop_api&refer=index_hot_new).*?title=\\"(.*?)\\">'
        raw_list = re.findall(pattern, self._html)
        for raw in raw_list:
            read_cnt, path, title = raw
            topic_list.append(
                {
                    'read_cnt': self.read_cnt_transfer(read_cnt),
                    'url': 'https://weibo.com/p/{}'.format(path),
                    'title': title.strip('#')
                }
            )
        return topic_list

    @staticmethod
    def read_cnt_transfer(read_cnt_str):
        if read_cnt_str.rstrip('亿') != read_cnt_str:
            return int(float(read_cnt_str.rstrip('亿')) * 100000000)
        elif read_cnt_str.rstrip('万') != read_cnt_str:
            return int(float(read_cnt_str.rstrip('万')) * 10000)
        else:
            return int(read_cnt_str)

    def get_numbers(self, url):
        """根据话题的url获取 阅读数, 讨论数, 粉丝数等数据
            进一步解析topic_list中的详情url
        """
        pass


if __name__ == '__main__':
    # cookies_list = [{'path': '/', 'domain': 'weibo.com', 'httpOnly': False, 'secure': False, 'name': 'YF-Page-G0', 'value': 'c47452adc667e76a7435512bb2f774f3'}, {'path': '/', 'expiry': 1524203180, 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'un', 'value': '17557285895'}, {'path': '/', 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'SSOLoginState', 'value': '1523339179'}, {'path': '/', 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'login_sid_t', 'value': '067977ead3526b6a8db79ea0815267dd'}, {'path': '/', 'expiry': 1554875180.343214, 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'SUBP', 'value': '0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh1c52cTZxmZGynR7Exju6P5JpX5K2hUgL.FoecSK-fS0qfehe2dJLoI7XLxK-L1K-L128.dciL'}, {'path': '/', 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'Apache', 'value': '7169741214867.205.1523339178551'}, {'path': '/', 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': '_s_tentry', 'value': '-'}, {'path': '/', 'expiry': 1554875180.343224, 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'SUHB', 'value': '0rr7gRDSdZGP3C'}, {'path': '/', 'domain': '.weibo.com', 'httpOnly': True, 'secure': False, 'name': 'SUB', 'value': '_2A253yD_8DeRhGeVI7lcU9yjJyz-IHXVUvBY0rDV8PUNbmtBeLW_QkW9NT2uPITh9xG72vmloQIdHQV4H8Tp1d34u'}, {'path': '/', 'expiry': 1523339776, 'domain': 'weibo.com', 'httpOnly': False, 'secure': False, 'name': 'WBStorage', 'value': 'b611234b8b979b26|undefined'}, {'path': '/', 'domain': 'weibo.com', 'httpOnly': False, 'secure': False, 'name': 'YF-V5-G0', 'value': '694581d81c495bd4b6d62b3ba4f9f1c8'}, {'path': '/', 'expiry': 1523943980.587113, 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'wvr', 'value': '6'}, {'path': '/', 'domain': 'weibo.com', 'httpOnly': False, 'secure': False, 'name': 'YF-Ugrow-G0', 'value': '169004153682ef91866609488943c77f'}, {'path': '/', 'expiry': 1838699179.34317, 'domain': '.weibo.com', 'httpOnly': True, 'secure': False, 'name': 'SCF', 'value': 'AiOhUjBjYU9ep9EYT2upUBczi12y4QV-7xrY2Y8x3YklrW11h2NkRsmis3KcYhhRezHFbPH4ZPnrhx2MCqYzunI.'}, {'path': '/', 'expiry': 1554875179.343258, 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'ALF', 'value': '1554875179'}, {'path': '/', 'expiry': 1554443178, 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'ULV', 'value': '1523339178556:1:1:1:7169741214867.205.1523339178551:'}, {'path': '/', 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'cross_origin_proto', 'value': 'SSL'}, {'path': '/', 'expiry': 1838699178, 'domain': '.weibo.com', 'httpOnly': False, 'secure': False, 'name': 'SINAGLOBAL', 'value': '7169741214867.205.1523339178551'}]
    # user_id1 = 3655576503
    # spd = HotNewTopicSpider(cookies_list, user_id1)
    # topic_list1 = spd.get_topic_list()
    # import json
    # print(json.dumps(topic_list1))

    chrome_driver_path1 = '/root/qk_python/python/data/collect/weibo_spider/priv/chromedriver'
    username1 = input('请输入你的账号\n')
    password1 = input('请输入你的密码\n')
    login_url1 = 'https://weibo.com/login.php'
    sl = WeiboSeleniumLogin(chrome_driver_path1)
    if sl.login(username1, password1, login_url1):
        print('login success')
        # print(sl.cookies)
        # print(sl.user_id)
    else:
        print('login failed')

    spd = HotNewTopicSpider(sl.cookies, sl.user_id)
    topic_list1 = spd.get_topic_list()
    import json
    print(json.dumps(topic_list1))
