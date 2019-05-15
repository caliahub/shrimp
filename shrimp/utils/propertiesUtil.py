#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time   :  2019/4/4
# @Author :  Calia
# @Email  :  percalia@qq.com
# 
# Properties配置文件


class Properties(object):
    @classmethod
    def getProperties(cls):
        """
        读取server.properties配置
        :return:
        """
        try:
            properties_file = open('server.properties', 'r', encoding='utf-8')
            properties = {}
            for line in properties_file:
                if line.find('=') > 0:
                    strs = line.replace('\n', '').split('=')
                    if strs[0].strip().startswith('#'):
                        continue
                    properties[strs[0].strip()] = strs[1].strip().lower()
        except Exception as e:
            raise e
        else:
            properties_file.close()
        return properties
