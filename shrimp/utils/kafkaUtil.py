#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-3-31
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# kafka工具类

import json
from kafka import KafkaProducer


class Producer(object):
    def __init__(self, servers):
        self.producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      bootstrap_servers=servers,
                                      compression_type='gzip')

    def send(self, topic, msg):
        """
        生产消息
        :return:
        """
        self.producer.send(topic=topic, value=msg)
        self.producer.flush()
