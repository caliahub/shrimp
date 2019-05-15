#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# 测试磁盘监控功能

import unittest
import json
from shrimp.service import DiskMonitor


class TestDiskMonitor(unittest.TestCase):
    def test_disk_partition(self):
        res = DiskMonitor.disk_partition()
        print('分区:')
        print(json.dumps(res))

    def test_disk_io(self):
        res = DiskMonitor.disk_io()
        print('IO:')
        print(json.dumps(res))


if __name__ == '__main__':
    unittest.main()
