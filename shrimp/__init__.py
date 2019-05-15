#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/3/28
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# flask初始化

from flask import Flask, Blueprint
from flask_apscheduler import APScheduler
from shrimp.utils.propertiesUtil import Properties

# 加载配置信息
app = Flask(__name__)
properties = Properties.getProperties()

# 启动定时任务
scheduler = APScheduler()
scheduler.start()

# 注册蓝图
blueprint_monitor = Blueprint('api_system', __name__, url_prefix='/system')
blueprint_task = Blueprint('api_task', __name__, url_prefix='/task')
from shrimp.api import *
app.register_blueprint(blueprint_task)
app.register_blueprint(blueprint_monitor)


# kafka服务
if 'on' == properties.get('kafka', None):
    from shrimp.task.task_kafka_collect import KafkaCollect
    from shrimp.utils.kafkaUtil import Producer
    producer = Producer(servers=properties.get('kafka.bootstrap.servers', None))
    kafkaCollect = KafkaCollect(properties=properties, scheduler=scheduler)
    kafkaCollect.start_collect()

# elasticsearch服务
if 'on' == properties.get('elasticsearch', None):
    from shrimp.task.task_elasticsearch_collect import ElasticsearchCollect
    from shrimp.utils.elasticsearchUtil import Elasticsearch
    elasticsearch = Elasticsearch(hosts=properties.get('elasticsearch.hosts', None))
    elasticsearchCollect = ElasticsearchCollect(properties=properties, scheduler=scheduler)
    elasticsearchCollect.start_collect()
