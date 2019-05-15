#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-3-30
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# CPU监控

import psutil


class CPUMonitor(object):

    @classmethod
    def cpu_time(cls):
        """
        CPU时间
        :return:
        """
        return psutil.cpu_times()._asdict()

    @classmethod
    def cpu_percent(cls, percpu=False):
        """
        CPU利用率
        :return:
        """
        return psutil.cpu_percent(interval=0.1, percpu=percpu)

    @classmethod
    def cpu_count(cls, logical=True):
        """
        CPU逻辑数量
        :return:
        """
        return psutil.cpu_count(logical=logical)

    @classmethod
    def cpu_stats(cls):
        """
        CPU统计信息
        :return:
        """
        return psutil.cpu_stats()._asdict()

    @classmethod
    def cpu_freq(cls, percpu=False):
        """
        CPU频率
        :return:
        """
        if percpu:
            freq_list = []
            for freq in psutil.cpu_freq(percpu=True):
                freq_list.append(freq._asdict())
            return freq_list
        else:
            return psutil.cpu_freq()._asdict()

    @classmethod
    def cpu_info(cls, percpu=False, logical=True):
        """
        CPU详细信息
        :return:
        """
        info = {
            'time': cls.cpu_time(),
            'percent': cls.cpu_percent(percpu=percpu),
            'count': cls.cpu_count(logical=logical),
            'stats': cls.cpu_stats(),
            'freq': cls.cpu_freq(percpu=percpu)
        }
        return info

    @classmethod
    def cpu_simple(cls):
        """
        CPU简略信息
        :return:
        """
        percent = cls.cpu_percent()
        cpu = {
            'percent': percent
        }
        return cpu