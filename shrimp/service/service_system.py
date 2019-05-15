#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# 基础监控

import platform
import psutil
import socket
from datetime import datetime


class SystemMonitor(object):
    @classmethod
    def boot_time(cls):
        """
        系统启动时间
        :return:
        """
        boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        return boot_time

    @classmethod
    def login_users(cls):
        """
        登录用户
        :return:
        """
        login_users = []
        for user in psutil.users():
            name = user.name
            terminal = user.terminal
            host = user.host
            started = datetime.fromtimestamp(user.started).strftime("%Y-%m-%d %H:%M:%S")
            pid = user.pid
            user_dict = {
                'name': name,
                'termianl': terminal,
                'host': host,
                'started': started,
                'pid': pid
            }
            login_users.append(user_dict)
        return login_users

    @classmethod
    def platform_info(cls):
        """
        系统基础信息
        :return:
        """
        platform_dict = platform.uname()._asdict()
        hostname = platform_dict['node']
        ip = socket.gethostbyname(hostname)
        del platform_dict['node']
        platform_dict['hostname'] = hostname
        platform_dict['ip'] = ip
        return platform_dict
