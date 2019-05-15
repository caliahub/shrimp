#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date   :  19-3-30
# @Author :  Calia
# @Email  :  percalia@qq.com
#
# 网络监控

import psutil
import time


class NetworkMonitor(object):

    @classmethod
    def network_io(cls):
        """
        网络IO
        :return:
        """
        net_io_counters = psutil.net_io_counters(pernic=True, nowrap=False)
        io_list = []
        for key, value in net_io_counters.items():
            bytes_sent = value.bytes_sent
            bytes_recv = value.bytes_recv
            packets_sent = value.packets_sent
            packets_recv = value.packets_recv
            errin = value.errin
            errout = value.errout
            dropin = value.dropin
            dropout = value.dropout
            io_dict = {
                'drive': key,
                'bytes_sent': bytes_sent,
                'bytes_recv': bytes_recv,
                'packets_sent': packets_sent,
                'packets_recv': packets_recv,
                'errin': errin,
                'errout': errout,
                'dropin': dropin,
                'dropout': dropout
            }
            io_list.append(io_dict)
        return io_list

    @classmethod
    def network_connections(cls):
        """
        网络连接数
        :return:
        """
        connection_list = []
        for connection in psutil.net_connections():
            fd = connection.fd
            family = connection.family
            ftype = connection.type
            laddr = connection.laddr
            raddr = connection.raddr
            status = connection.status
            pid = connection.pid
            lip = '' if not laddr else laddr[0]
            lport = '' if not laddr else laddr[1]
            rip = '' if not raddr else raddr[0]
            rport = '' if not raddr else raddr[1]
            connection_dict = {
                'fd': fd,
                'family': family.name,
                'type': ftype,
                'lip': lip,
                'lport': lport,
                'rip': rip,
                'rport': rport,
                'status': status,
                'pid': pid
            }
            connection_list.append(connection_dict)
        return connection_list

    @classmethod
    def network_addr(cls):
        """
        网卡地址
        :return:
        """
        addrs = psutil.net_if_addrs()
        addr_list = []
        for key, value in addrs.items():
            v_list = []
            for v in value:
                family = v.family.name
                address = v.address
                netmask = v.netmask
                broadcast = v.broadcast
                ptp = v.ptp
                v_dict = {
                    'family': family,
                    'address': address,
                    'netmask': netmask,
                    'broadcast': broadcast,
                    'ptp': ptp
                }
                v_list.append(v_dict)
            addr = {
                'device': key,
                'addrs': v_list
            }
            addr_list.append(addr)
        return addr_list

    @classmethod
    def network_info(cls):
        """
        网络详细信息
        :return:
        """
        info = {
            'io': cls.network_io(),
            'connection': cls.network_connections(),
            'addr': cls.network_addr()
        }
        return info

    @classmethod
    def network_simple(cls):
        """
        网络简略信息
        :return:
        """
        from shrimp.service import SystemMonitor
        ip = SystemMonitor.platform_info()['ip']
        drive = None
        addr_list = cls.network_addr()
        for addr in addr_list:
            for a in addr['addrs']:
                if 'AF_INET' == a['family'] and ip == a['address']:
                        drive = addr['device']
                        break
        io_list_1 = cls.network_io()
        time.sleep(1)
        io_list_2 = cls.network_io()
        io = {}
        for io_1, io_2 in zip(io_list_1, io_list_2):
            if drive == io_1['drive']:
                bytes_sent_1 = io_1['bytes_sent']
                bytes_recv_1 = io_1['bytes_recv']
                bytes_sent_2 = io_2['bytes_sent']
                bytes_recv_2 = io_2['bytes_recv']
                bytes_sent_sec = bytes_sent_2 - bytes_sent_1
                bytes_recv_sec = bytes_recv_2 - bytes_recv_1
                packets_sent_1 = io_1['packets_sent']
                packets_recv_1 = io_1['packets_recv']
                packets_sent_2 = io_2['packets_sent']
                packets_recv_2 = io_2['packets_recv']
                packets_sent_sec = packets_sent_2 - packets_sent_1
                packets_recv_sec = packets_recv_2 - packets_recv_1
                io = {
                    'drive': drive,
                    'bytes_sent_sec': bytes_sent_sec,
                    'bytes_recv_sec': bytes_recv_sec,
                    'packets_sent_sec': packets_sent_sec,
                    'packets_recv_sec': packets_recv_sec
                }
                break

        connections_list = cls.network_connections()
        from shrimp.service import SystemMonitor
        ip = SystemMonitor.platform_info()['ip']
        tcp_total = 0
        established = 0
        for connections in connections_list:
            if ip == connections['lip']:
                tcp_total += 1
                if 'ESTABLISHED' == connections['status']:
                    established += 1
        non_established = tcp_total - established
        connections = {
            'established': established,
            'non_established': non_established,
            'tcp_total': tcp_total
        }
        network = {
            'io': io,
            'connections': connections
        }
        return network
