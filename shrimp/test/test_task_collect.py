#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# 测试监控定时任务功能

import unittest
from shrimp.task import *


class TestTaskCollect(unittest.TestCase):
    def test_collect_cpu(self):
        collect_cpu()

    def test_collect_memory(self):
        collect_memory()

    def test_collect_disk(self):
        collect_disk()

    def test_collect_network(self):
        collect_network()

    def test_collect_process(self):
        collect_process()


if __name__ == '__main__':
    unittest.main()
