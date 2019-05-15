#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# api接口

from shrimp.api import api_system
from shrimp.api import api_task_kafka
from shrimp.api import api_task_elasticsearch

__all__ = [
    'api_system',
    'api_task_kafka',
    'api_task_elasticsearch'
]
