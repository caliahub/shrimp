#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# 测试基础监控功能

import unittest
import json
from shrimp.service import SystemMonitor


class TestSystemMonitor(unittest.TestCase):
    def test_cpu(self):
        res = SystemMonitor.cpu()
        print('CPU:')
        print(json.dumps(res))

    def test_memory(self):
        res = SystemMonitor.memory()
        print('内存:')
        print(json.dumps(res))

    def test_disk(self):
        res = SystemMonitor.disk()
        print('磁盘:')
        print(json.dumps(res))

    def test_network(self):
        res = SystemMonitor.network()
        print('网络:')
        print(json.dumps(res))

    def test_boot_time(self):
        res = SystemMonitor.boot_time()
        print('启动时间:')
        print(res)

    def test_login_users(self):
        res = SystemMonitor.login_users()
        print('登录用户:')
        print(json.dumps(res))

    def test_base_info(self):
        res = SystemMonitor.platform_info()
        print('基础信息:')
        print(json.dumps(res))


if __name__ == '__main__':
    unittest.main()
