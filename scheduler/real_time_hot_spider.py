#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 4/3/18 2:08 PM
@author: Chen Liang
@function: 爬取weibo实时热搜榜（不需要登录）
"""

from spider.base_spider import BaseSpider
import re
from urllib import parse
import json
import sys


class RealTimeHotSpider(BaseSpider):
    """爬取weibo实时热搜榜（不需要登录）"""
    def get_hot_list(self, url):
        html = self.get_html_content(url)
        raw = re.findall(r'class=\\"star_name\\">.*?<a href=\\"\\/weibo\\/(.*?)&Refer=[top|new]', html)
        hot_degree_lst = re.findall(r'class=\\"star_num\\"><span>(.*?)<\\/span>', html)
        hot_degree_lst.insert(0, sys.maxsize)
        title_lst = []
        names_lst = []
        links_lst = []

        for i in raw:
            title_lst.append(i.replace('25', ''))

        for i in title_lst:
            names_lst.append(parse.unquote(i))
            link = 'http://s.weibo.com/weibo/' + i
            links_lst.append(link)

        hot_info = []
        for i, v in enumerate(names_lst):
            # print(i, v, links_lst[i], hot_degree_lst[i])
            json_data = {
                "number": i,
                "title": v,
                "url": links_lst[i],
                "hot": hot_degree_lst[i]
            }
            hot_info.append(json_data)
        return json.dumps(hot_info)


if __name__ == '__main__':
    spider = RealTimeHotSpider()
    target_real_time_hot = 'http://s.weibo.com/top/summary?cate=realtimehot'
    print(spider.get_hot_list(target_real_time_hot))
