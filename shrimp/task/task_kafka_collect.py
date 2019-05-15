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
    from shrimp import producer, properties
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
    producer.send(topic=properties.get('kafka.topic.system', 'shrimp-system'), msg=json.dumps(data))


class KafkaCollect(object):
    def __init__(self, properties, scheduler):
        self.kafka = False
        if 'on' == properties.get('kafka', 'off'):
            self.kafka = True
        self.scheduler = scheduler
        self.freq = properties.get('kafka.collect.freq', '30')

    def start_collect(self):
        """
        启动采集任务
        :return:
        """
        if self.kafka and self.freq is not None and self.freq.isdigit():
            self.freq = int(self.freq)
            self.scheduler.add_job('jod_kafka_system', collect_system, trigger='interval', seconds=self.freq)
