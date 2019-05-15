#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# 测试CPU监控功能

import unittest
import json
from shrimp.service import CPUMonitor


class TestCPUMonitor(unittest.TestCase):
    def test_cpu_time(self):
        res = CPUMonitor.cpu_time()
        print('时间:')
        print(json.dumps(res))

    def test_cpu_percent(self):
        res = CPUMonitor.cpu_percent(percpu=True)
        print('使用率:')
        print(res)

    def test_cpu_count(self):
        res = CPUMonitor.cpu_count(logical=False)
        print('核数:')
        print(res)

    def test_cpu_stats(self):
        res = CPUMonitor.cpu_stats()
        print('统计信息：')
        print(json.dumps(res))

    def test_cpu_freq(self):
        res = CPUMonitor.cpu_freq(percpu=True)
        print('频率：')
        print(json.dumps(res))

    def test_cpu_info(self):
        res = CPUMonitor.cpu_info(percpu=True, logical=True)
        print('信息：')
        print(json.dumps(res))


if __name__ == '__main__':
    unittest.main()
