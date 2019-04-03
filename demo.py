# -*- coding:utf-8 -*-
import json

__author__ = 'zhoujifeng'
__date__ = '2019/4/3 20:09'

if __name__ == '__main__':
    path = './static/json/city.json'
    with open(path, 'r+', encoding='utf-8') as r:
        city = json.loads(r.read())
    print(list(city['city'].values()))
