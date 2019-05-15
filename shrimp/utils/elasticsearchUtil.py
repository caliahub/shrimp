#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-4-13
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# elasticsearch工具类

from elasticsearch import Elasticsearch as es


class Elasticsearch(object):

    def __init__(self, hosts):
        self.client = es(hosts=[hosts])

    def add(self, index, doc):
        """
        插入数据
        :param index: 
        :param doc: 
        :return: 
        """
        self.client.index(index=index, doc_type='_doc', body=doc)
