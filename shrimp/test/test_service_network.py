#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# 测试网络监控功能

import unittest
import json
from shrimp.service import NetworkMonitor


class TestDiskMonitor(unittest.TestCase):
    def test_network_io(self):
        res = NetworkMonitor.network_io()
        print('IO:')
        print(json.dumps(res))

    def test_network_connection(self):
        res = NetworkMonitor.network_connections()
        print('连接数:')
        print(json.dumps(res))

    def test_network_addr(self):
        res = NetworkMonitor.network_addr()
        print('网卡')
        print(json.dumps(res))


if __name__ == '__main__':
    unittest.main()
