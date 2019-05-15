#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/4
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# kafka定时任务接口

import json
from flask import request, abort
from shrimp import scheduler, properties, blueprint_task


@blueprint_task.route('/kafka/<info>/', methods=['GET'])
def get_kafka_task(info):
    """
    获取采集定时任务状态
    :return:
    """
    if info not in {'system', }:
        abort(404)
    if 'on' != properties.get('kafka', 'off'):
        return json.dumps({'status': 'fail', 'msg': '未启用该采集功能'})
    # 获取system采集任务
    if 'system' == info:
        jod_kafka_system = scheduler.get_job('jod_kafka_system')
        if jod_kafka_system is None:
            return json.dumps({'status': 'success', 'code': 0, 'msg': '采集任务未启动'})
        else:
            return json.dumps({'status': 'success', 'code': 1, 'jod': str(jod_kafka_system)})


@blueprint_task.route('/kafka/<info>/', methods=['POST'])
def update_kafka_task(info):
    """
    更新或启动采集定时任务
    :param info:
    :return:
    """
    if info not in {'system', }:
        abort(404)
    if 'on' != properties.get('kafka', 'off'):
        return json.dumps({'status': 'fail', 'msg': '未启用该采集功能'})
    # 获取定时任务参数
    data = request.get_data()
    if len(data) == 0:
        return json.dumps({'status': 'fail', 'msg': '参数错误'})
    try:
        jsondata = json.loads(data)
        seconds = jsondata['seconds']
        if not isinstance(seconds, int):
            return json.dumps({'status': 'fail', 'msg': 'seconds参数类型错误'})
        # 更改system采集任务
        if 'system' == info:
            from shrimp.task.task_kafka_collect import collect_system
            jod_kafka_system = scheduler.get_job('jod_kafka_system')
            if jod_kafka_system is None:
                jod = scheduler.add_job('jod_kafka_cpu', collect_system, trigger='interval', seconds=seconds)
                return json.dumps({'status': 'success', 'code': 1, 'jod': str(jod)})
            else:
                scheduler.modify_job('jod_kafka_system', trigger='interval', seconds=seconds)
                return json.dumps({'status': 'success', 'code': 1, 'jod': str(jod_kafka_system)})
    except KeyError:
        return json.dumps({'status': 'fail', 'msg': 'seconds参数不存在'})


@blueprint_task.route('/kafka/<info>/', methods=['DELETE'])
def delete_kafka_task(info):
    """
    删除采集任务
    :param info:
    :return:
    """
    if info not in {'system', }:
        abort(404)
    if 'on' != properties.get('kafka', 'off'):
        return json.dumps({'status': 'fail', 'msg': '未启用该采集功能'})
    try:
        # 关闭system采集任务
        if 'system' == info:
            jod_kafka_system = scheduler.get_job('jod_kafka_system')
            if jod_kafka_system is None:
                return json.dumps({'status': 'success', 'msg': '采集任务未启动'})
            else:
                scheduler.remove_job('jod_kafka_system')
                return json.dumps({'status': 'success', 'msg': '采集任务关闭成功', 'jod': str(jod_kafka_system)})
    except (BaseException,):
        return json.dumps({'status': 'fail', 'msg': '采集任务关闭失败'})
