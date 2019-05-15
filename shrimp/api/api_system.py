#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# 系统接口

import json
from flask import Blueprint, request, abort
from shrimp import blueprint_monitor


@blueprint_monitor.route('/', methods=['GET'])
def system_base_info():
    """
    基础信息接口
    :return:
    """
    from shrimp.service import SystemMonitor
    boot_time = SystemMonitor.boot_time()
    platform = SystemMonitor.platform_info()
    login_users = SystemMonitor.login_users()
    data = {
        'boot_time': boot_time,
        'platform': platform,
        'login_users': login_users
    }
    return json.dumps(data)


@blueprint_monitor.route('/<info>/', methods=['GET'])
def system_simple_info(info):
    """
    基本信息接口
    :param info:
    :return:
    """
    from shrimp.service import SystemMonitor, CPUMonitor, MemoryMonitor, DiskMonitor, NetworkMonitor, ProcessMonitor
    if 'boot_time' == info:
        data = {
            'boot_time': SystemMonitor.boot_time()
        }
        return json.dumps(data)
    elif 'platform' == info:
        return json.dumps(SystemMonitor.platform_info())
    elif 'login_users' == info:
        return json.dumps(SystemMonitor.login_users())
    elif 'cpu' == info:
        return json.dumps(CPUMonitor.cpu_simple())
    elif 'memory' == info:
        return json.dumps(MemoryMonitor.memory_simple())
    elif 'disk' == info:
        return json.dumps(DiskMonitor.disk_simple())
    elif 'network' == info:
        return json.dumps(NetworkMonitor.network_simple())
    elif 'process' == info:
        num = request.args.get('num')
        if num is not None and num.isdigit():
            return json.dumps(ProcessMonitor.process_simple(num=int(num)))
        else:
            return json.dumps(ProcessMonitor.process_simple())
    else:
        abort(404)


@blueprint_monitor.route('/cpu/<info>/', methods=['GET'])
def system_cpu_info(info):
    """
    CPU信息接口
    :param info:
    :return:
    """
    from shrimp.service import CPUMonitor
    percpu = False
    if 'true' == request.args.get('percpu'):
        percpu = True
    logical = True
    if 'false' == request.args.get('logical'):
        logical = False

    if 'time' == info:
        return json.dumps(CPUMonitor.cpu_time())
    elif 'percent' == info:
        percent = {
            'percent': CPUMonitor.cpu_percent(percpu=percpu)
        }
        return json.dumps(percent)
    elif 'count' == info:
        count = {
            'count': CPUMonitor.cpu_count(logical=logical)
        }
        return json.dumps(count)
    elif 'stats' == info:
        return json.dumps(CPUMonitor.cpu_stats())
    elif 'freq' == info:
        return json.dumps(CPUMonitor.cpu_freq(percpu=percpu))
    elif 'info' == info:
        return json.dumps(CPUMonitor.cpu_info(percpu=percpu, logical=logical))
    else:
        abort(404)


@blueprint_monitor.route('/memory/<info>/', methods=['GET'])
def system_memory_info(info):
    """
    内存信息接口
    :param info:
    :return:
    """
    from shrimp.service import MemoryMonitor
    if 'virtual' == info:
        return json.dumps(MemoryMonitor.virtual_memory())
    elif 'swap' == info:
        return json.dumps(MemoryMonitor.swap_memory())
    elif 'info' == info:
        return json.dumps(MemoryMonitor.memory_info())
    else:
        abort(404)


@blueprint_monitor.route('/disk/<info>/', methods=['GET'])
def system_disk_info(info):
    """
    磁盘信息接口
    :param info:
    :return:
    """
    from shrimp.service import DiskMonitor
    if 'partition' == info:
        return json.dumps(DiskMonitor.disk_partition())
    elif 'io' == info:
        return json.dumps(DiskMonitor.disk_io())
    elif 'info' == info:
        return json.dumps(DiskMonitor.disk_info())
    else:
        abort(404)


@blueprint_monitor.route('/network/<info>/', methods=['GET'])
def system_network_info(info):
    """
    网络信息接口
    :param info:
    :return:
    """
    from shrimp.service import NetworkMonitor
    if 'io' == info:
        return json.dumps(NetworkMonitor.network_io())
    elif 'connections' == info:
        return json.dumps(NetworkMonitor.network_connections())
    elif 'addr' == info:
        return json.dumps(NetworkMonitor.network_addr())
    elif 'info' == info:
        return json.dumps(NetworkMonitor.network_info())
    else:
        abort(404)


@blueprint_monitor.route('/process/<info>/', methods=['GET'])
def system_process_info(info):
    """
    进程信息接口
    :param info:
    :return:
    """
    from shrimp.service import ProcessMonitor
    simple = True
    if 'false' == request.args.get('simple'):
        simple = False
    if info.isdigit():
        return json.dumps(ProcessMonitor.process_pid(pid=int(info)))
    elif 'info' == info:
        return json.dumps(ProcessMonitor.process_list(simple=simple))
    else:
        abort(404)


@blueprint_monitor.route('/process/<pid>/<info>', methods=['GET'])
def system_process_pid_info(pid, info):
    """
    进程各项信息接口
    :param pid:
    :param info:
    :return:
    """
    from shrimp.service import ProcessMonitor
    if pid.isdigit():
        return json.dumps(ProcessMonitor.process_pid_info(pid=int(pid), info=info))
    else:
        abort(404)
