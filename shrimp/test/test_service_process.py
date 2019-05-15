#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# 测试Process功能

import unittest
import json
from shrimp.service import ProcessMonitor


class TestProcessMonitor(unittest.TestCase):
    # def test_process_list(self):
    #     res = ProcessMonitor.process_list(simple=True)
    #     print('进程列表：')
    #     print(json.dumps(res))
    #
    # def test_process_pid(self):
    #     res = ProcessMonitor.process_pid(pid=9980)
    #     print('进程信息：')
    #     print(json.dumps(res))
    #
    # def test_process_pid_info(self):
    #     res = ProcessMonitor.process_pid_info(pid=5148, info='is_running')
    #     print('进程各项参数:')
    #     print(res)

    def test_process_simple(self):
        res = ProcessMonitor.process_simple()
        print(json.dumps(res))


if __name__ == '__main__':
    unittest.main()
