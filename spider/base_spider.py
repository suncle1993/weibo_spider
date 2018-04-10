#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 4/3/18 5:00 PM
@author: Chen Liang
@function: 基础请求模块
"""

import requests


class BaseSpider(object):
    @staticmethod
    def get_html_content(url, cookies=None):
        """

        :param url:
        :param cookies: cookies for request: dict
        :return:
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'
        }
        try:
            if cookies is None:
                r = requests.get(url, headers=headers)
            else:
                r = requests.get(url, headers=headers, cookies=cookies)
            if r.status_code == 200:
                r.encoding = 'utf-8'  # 这一行是将编码转为utf-8否则中文会显示乱码。
                return r.text
        except Exception as e:
            print(str(e))
        return ''
