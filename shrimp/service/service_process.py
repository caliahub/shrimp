#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-3-30
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# 进程监控

import psutil
from datetime import datetime


class ProcessMonitor(object):

    @classmethod
    def process_list(cls, simple=True):
        """
        进程详细列表
        :return:
        """
        process_list = []
        for process in psutil.process_iter():
            try:
                if simple:
                    process_dict = process.as_dict(attrs=['pid', 'name', 'username'])
                else:
                    process_dict = process.as_dict()
            except psutil.NoSuchProcess:
                pass
            else:
                process_list.append(process_dict)
        return process_list

    @classmethod
    def process_pid(cls, pid):
        """
        单进程详细列表
        :return:
        """
        try:
            proc = psutil.Process(pid=pid)
            return proc.as_dict()
        except psutil.NoSuchProcess:
            return ''

    @classmethod
    def process_pid_info(cls, pid, info):
        """
        单进程各项信息
        :return:
        """
        try:
            p = psutil.Process(pid=pid)
            if 'ppid' == info:
                # 进程父PID
                return p.ppid
            elif 'name' == info:
                # 进程名称
                return p.name()
            elif 'exe' == info:
                # 该进程执行绝对路径
                return p.exe()
            elif 'cmdline' == info:
                # 执行命令
                return p.cmdline()
            elif 'environ' == info:
                # 环境变量
                return p.environ()
            elif 'create_time' == info:
                # 创建时间
                return datetime.fromtimestamp(p.create_time()).strftime("%Y-%m-%d %H:%M:%S")
            elif 'parent' == info:
                # 父进程
                return p.parent().as_dict()
            elif 'status' == info:
                # 进程状态
                return p.status()
            elif 'cwd' == info:
                # 进程当前工作目录
                return p.cwd()
            elif 'username' == info:
                # 拥有该进程用户的名称
                return p.username()
            elif 'nice' == info:
                # 进程优先级
                return p.nice()
            elif 'ionice' == info:
                # 进程IO优先级
                return p.ionice()
            elif 'io_counters' == info:
                # 进程IO统计信息
                return p.io_counters()
            elif 'num_ctx_switches' == info:
                # 上下文切换次数
                return p.num_ctx_switches()
            elif 'num_handles' == info:
                # 句柄数
                return p.num_handles()
            elif 'num_threads' == info:
                # 线程数
                return p.num_threads()
            elif 'threads' == info:
                # 相关线程
                thread_list = []
                for thread in p.threads():
                    thread_list.append(thread._asdict())
                return thread_list
            elif 'cpu_percent' == info:
                # CPU频率
                from shrimp.service import CPUMonitor
                percent = p.cpu_percent(interval=0.1)
                count = CPUMonitor.cpu_count(logical=True)
                return percent/count
            elif 'memory_info' == info:
                # 内存信息
                return p.memory_info()._asdict()
            elif 'open_files' == info:
                # 进程所打开的文件
                file_list = []
                for file in p.open_files():
                    file_list.append(file._asdict())
                return file_list
            elif 'connections' == info:
                # 套接字连接
                conn_list = []
                for conn in p.connections():
                    conn_list.append(conn._asdict())
                return conn_list
            elif 'is_running' == info:
                # 进程是否存在
                return p.is_running()
        except psutil.NoSuchProcess:
            return ''

    @classmethod
    def process_simple(cls, num=10):
        """
        进程简略信息
        :return:
        """
        process_list = []
        for p in sorted(psutil.process_iter(attrs=['name', 'memory_percent']),
                        key=lambda p: p.info['memory_percent'])[-num:]:
            try:
                pid = p.pid
                name = p.name()
                username = p.username()
                cpu_percent = p.cpu_percent(interval=0.1)
                memory_percent = p.memory_percent()
                num_openfiles = len(p.open_files())
                num_threads = p.num_threads()
                process_dict = {
                    'pid': pid,
                    'name': name,
                    'username': username,
                    'cpu_percent': cpu_percent,
                    'memory_percent': memory_percent,
                    'num_openfiles': num_openfiles,
                    'num_threads': num_threads
                }
                process_list.append(process_dict)
            except (BaseException,):
                continue
        return process_list


