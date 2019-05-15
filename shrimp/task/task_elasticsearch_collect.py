#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-3-31
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# 采集定时任务


def collect_system():
    """
    采集system信息
    :return: 
    """
    import json
    from datetime import datetime
    from shrimp import elasticsearch, properties
    from shrimp.service import SystemMonitor, CPUMonitor, MemoryMonitor, DiskMonitor, NetworkMonitor,ProcessMonitor
    platform = SystemMonitor.platform_info()
    data = {
        'ip': platform['ip'],
        'hostname': platform['hostname'],
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'cpu': CPUMonitor.cpu_simple(),
        'memory': MemoryMonitor.memory_simple(),
        'disk': DiskMonitor.disk_simple(),
        'network': NetworkMonitor.network_simple(),
        'process': ProcessMonitor.process_simple(num=15)
    }
    elasticsearch.add(index=properties.get('elasticsearch.index.system', 'shrimp-system'), doc=json.dumps(data))


class ElasticsearchCollect(object):
    def __init__(self, properties, scheduler):
        self.elasticsearch = False
        if 'on' == properties.get('elasticsearch', 'off'):
            self.elasticsearch = True
        self.scheduler = scheduler
        self.freq = properties.get('elasticsearch.collect.freq', '30')

    def start_collect(self):
        """
        启动采集任务
        :return:
        """
        if self.elasticsearch and self.freq is not None and self.freq.isdigit():
            self.freq = int(self.freq)
            self.scheduler.add_job('jod_elasticsearch_system', collect_system, trigger='interval',  seconds=self.freq)
