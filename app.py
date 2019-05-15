#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# 入口文件

import datetime
from shrimp import app, properties


@app.route('/')
def index():
    return '%s\t欢迎访问monitor项目' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    app.run(properties['server.ip'], int(properties['server.port']))
