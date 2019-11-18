# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq


def get_html(url, code="utf-8"):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        # print("test")
        return r.text
    except Exception as e:
        print(e)
        return " "


def main(name):
    search_name_url = "http://www.baidu.com/s?wd=" + name

    doc = pq(get_html(search_name_url))

    search_list = doc('#content_left h3.t a').items()
    i = 0
    for li in search_list:
        i += 1
        print('标题：' + li.text())
        print('链接：' + li.attr('href'))
        print("")
    # print(i)


if __name__ == '__main__':
    main("赵静")
