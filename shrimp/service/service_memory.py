#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-3-30
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# 内存监控

import psutil


class MemoryMonitor(object):

    @classmethod
    def virtual_memory(cls):
        """
        物理内存
        :return:
        """
        return psutil.virtual_memory()._asdict()

    @classmethod
    def swap_memory(cls):
        """
        交换内存
        :return:
        """
        return psutil.swap_memory()._asdict()

    @classmethod
    def memory_info(cls):
        """
        内存详细信息
        :return:
        """
        info = {
            'virtual': cls.virtual_memory(),
            'swap': cls.swap_memory()
        }
        return info

    @classmethod
    def memory_simple(cls):
        """
        内存简略信息
        :return:
        """
        virtual_memory = cls.virtual_memory()
        virtual_percent = virtual_memory['percent']
        memory = {
            'percent': virtual_percent
        }
        return memory
