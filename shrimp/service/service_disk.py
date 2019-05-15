#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-3-30
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# 磁盘监控

import psutil
import time


class DiskMonitor(object):
    @classmethod
    def disk_partition(cls):
        """
        磁盘分区
        :return:
        """
        partition_list = []
        for partition in psutil.disk_partitions():
            device = partition.device
            mountpoint = partition.mountpoint
            fstype = partition.fstype
            opts = partition.opts
            usage = psutil.disk_usage(mountpoint)
            total = usage[0]
            used = usage[1]
            free = usage[2]
            percent = usage[3]
            partition_dict = {
                'device': device,
                'mountpoint': mountpoint,
                'fstype': fstype,
                'opts': opts,
                'total': total,
                'used': used,
                'free': free,
                'percent': percent
            }
            partition_list.append(partition_dict)
        return partition_list

    @classmethod
    def disk_io(cls):
        """
        磁盘IO
        :return:
        """
        io = psutil.disk_io_counters(perdisk=True, nowrap=False)
        io_list = []
        for key, value in io.items():
            read_count = value.read_count
            write_count = value.write_count
            read_bytes = value.read_bytes
            write_bytes = value.write_bytes
            read_time = value.read_time
            write_time = value.write_time
            io_dict = {
                'drive': key,
                'read_count': read_count,
                'write_count': write_count,
                'read_bytes': read_bytes,
                'write_bytes': write_bytes,
                'read_time': read_time,
                'write_time': write_time
            }
            io_list.append(io_dict)
        return io_list

    @classmethod
    def disk_info(cls):
        """
        磁盘详细信息
        :return:
        """
        info = {
            'partition': cls.disk_partition(),
            'io': cls.disk_io()
        }
        return info

    @classmethod
    def disk_simple(cls):
        """
        磁盘简略信息
        :return:
        """
        partition_list = cls.disk_partition()
        disk_partition = []
        for partition in partition_list:
            device = partition['device']
            percent = partition['percent']
            partition_dict = {
                'device': device,
                'percent': percent
            }
            disk_partition.append(partition_dict)

        io_list_1 = cls.disk_io()
        time.sleep(1)
        io_list_2 = cls.disk_io()
        disk_io = []
        for (io_1, io_2) in zip(io_list_1, io_list_2):
            drive = io_1['drive']
            read_bytes_1 = io_1['read_bytes']
            write_bytes_1 = io_1['write_bytes']
            read_count_1 = io_1['read_count']
            write_count_1 = io_1['write_count']
            read_bytes_2 = io_2['read_bytes']
            write_bytes_2 = io_2['write_bytes']
            read_count_2 = io_2['read_count']
            write_count_2 = io_2['write_count']
            bytes_read_sec = read_bytes_2 - read_bytes_1
            bytes_write_sec = write_bytes_2 - write_bytes_1
            count_read_sec = read_count_2 - read_count_1
            count_write_sec = write_count_2 - write_count_1
            disk_dict = {
                'drive': drive,
                'bytes_read_sec': bytes_read_sec,
                'bytes_write_sec': bytes_write_sec,
                'count_read_sec': count_read_sec,
                'count_write_sec': count_write_sec
            }
            disk_io.append(disk_dict)

        disk = {
            'partition': disk_partition,
            'io': disk_io
        }
        return disk
