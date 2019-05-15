## 磁盘信息接口

### 目录
- [网络基本信息](#网络基本信息)
- [网络IO](#网络IO)
- [网络连接数](#网络连接数)
- [网卡地址](#网卡地址)
- [网络完整信息](#网络完整信息)

#### 网络基本信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/network
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "io": {
        "drive": "本地连接",
        "bytes_sent_sec": 4102,
        "bytes_recv_sec": 4923,
        "packets_sent_sec": 24,
        "packets_recv_sec": 44
    },
    "connections": {
        "established": 38,
        "non_established": 33,
        "tcp_total": 71
    }
}
```

#### 网络IO
> 请求示例
```http
GET http://127.0.0.1:5000/system/network/io
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
[
    {
        "drive": "本地连接",
        "bytes_sent": 336356642,
        "bytes_recv": 1234226099,
        "packets_sent": 1471229,
        "packets_recv": 3791015,
        "errin": 0,
        "errout": 0,
        "dropin": 0,
        "dropout": 0
    },
    {
        "drive": "本地连接 2",
        "bytes_sent": 3194583,
        "bytes_recv": 18017450,
        "packets_sent": 21071,
        "packets_recv": 15485,
        "errin": 0,
        "errout": 0,
        "dropin": 0,
        "dropout": 0
    }
]
```

#### 网络连接数
> 请求示例
```http
GET http://127.0.0.1:5000/system/network/connections
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                           |
> 响应示例
```json
[
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 2,
        "lip": "192.168.152.1",
        "lport": 5353,
        "rip": "",
        "rport": "",
        "status": "NONE",
        "pid": 1708
    },
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 1,
        "lip": "0.0.0.0",
        "lport": 445,
        "rip": "",
        "rport": "",
        "status": "LISTEN",
        "pid": 4
    },
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 1,
        "lip": "192.168.0.83",
        "lport": 50254,
        "rip": "14.17.41.210",
        "rport": 80,
        "status": "CLOSE_WAIT",
        "pid": 5112
    },
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 1,
        "lip": "192.168.0.83",
        "lport": 139,
        "rip": "",
        "rport": "",
        "status": "LISTEN",
        "pid": 4
    },
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 1,
        "lip": "127.0.0.1",
        "lport": 54530,
        "rip": "127.0.0.1",
        "rport": 61561,
        "status": "ESTABLISHED",
        "pid": 3312
    },
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 1,
        "lip": "192.168.0.83",
        "lport": 62671,
        "rip": "216.58.200.238",
        "rport": 443,
        "status": "SYN_SENT",
        "pid": 3040
    },
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 1,
        "lip": "192.168.0.83",
        "lport": 62430,
        "rip": "47.107.207.138",
        "rport": 3306,
        "status": "ESTABLISHED",
        "pid": 1040
    },
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 1,
        "lip": "192.168.0.83",
        "lport": 54291,
        "rip": "120.26.105.188",
        "rport": 443,
        "status": "ESTABLISHED",
        "pid": 5496
    },
    {
        "fd": -1,
        "family": "AF_INET",
        "type": 2,
        "lip": "0.0.0.0",
        "lport": 53876,
        "rip": "",
        "rport": "",
        "status": "NONE",
        "pid": 5112
    }
]
```

#### 网卡地址
> 请求示例
```http
GET http://127.0.0.1:5000/system/network/addr
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                           |
> 响应示例
```json
[
     {
        "device": "本地连接",
        "addrs": [
            {
                "family": "AF_LINK",
                "address": "D4-3D-7E-9A-89-86",
                "netmask": null,
                "broadcast": null,
                "ptp": null
            },
            {
                "family": "AF_INET",
                "address": "192.168.0.83",
                "netmask": "255.255.255.0",
                "broadcast": null,
                "ptp": null
            },
            {
                "family": "AF_INET6",
                "address": "fe80::f8f4:f54d:5633:875d",
                "netmask": null,
                "broadcast": null,
                "ptp": null
            }
        ]
    },
    {
        "device": "本地连接 2",
        "addrs": [
            {
                "family": "AF_LINK",
                "address": "00-FF-C9-D3-6B-11",
                "netmask": null,
                "broadcast": null,
                "ptp": null
            },
            {
                "family": "AF_INET",
                "address": "2.0.1.10",
                "netmask": "255.255.255.0",
                "broadcast": null,
                "ptp": null
            },
            {
                "family": "AF_INET6",
                "address": "fe80::7cc0:e649:79b3:dccc",
                "netmask": null,
                "broadcast": null,
                "ptp": null
            }
        ]
    }
]
```

#### 网络完整信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/network/info
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "io": [
        {
            "drive": "本地连接",
            "bytes_sent": 336444798,
            "bytes_recv": 1234765807,
            "packets_sent": 1471911,
            "packets_recv": 3794690,
            "errin": 0,
            "errout": 0,
            "dropin": 0,
            "dropout": 0
        },
        {
            "drive": "本地连接 2",
            "bytes_sent": 3197660,
            "bytes_recv": 18017450,
            "packets_sent": 21087,
            "packets_recv": 15485,
            "errin": 0,
            "errout": 0,
            "dropin": 0,
            "dropout": 0
        }
    ],
    "connection": [
        {
            "fd": -1,
            "family": "AF_INET",
            "type": 2,
            "lip": "192.168.15.1",
            "lport": 60347,
            "rip": "",
            "rport": "",
            "status": "NONE",
            "pid": 5684
        },
        {
            "fd": -1,
            "family": "AF_INET",
            "type": 1,
            "lip": "127.0.0.1",
            "lport": 61563,
            "rip": "127.0.0.1",
            "rport": 61562,
            "status": "ESTABLISHED",
            "pid": 3312
        }
    ],
    "addr": [
{
            "device": "本地连接",
            "addrs": [
                {
                    "family": "AF_LINK",
                    "address": "D4-3D-7E-9A-89-86",
                    "netmask": null,
                    "broadcast": null,
                    "ptp": null
                },
                {
                    "family": "AF_INET",
                    "address": "192.168.0.83",
                    "netmask": "255.255.255.0",
                    "broadcast": null,
                    "ptp": null
                },
                {
                    "family": "AF_INET6",
                    "address": "fe80::f8f4:f54d:5633:875d",
                    "netmask": null,
                    "broadcast": null,
                    "ptp": null
                }
            ]
        },
        {
            "device": "本地连接 2",
            "addrs": [
                {
                    "family": "AF_LINK",
                    "address": "00-FF-C9-D3-6B-11",
                    "netmask": null,
                    "broadcast": null,
                    "ptp": null
                },
                {
                    "family": "AF_INET",
                    "address": "2.0.1.10",
                    "netmask": "255.255.255.0",
                    "broadcast": null,
                    "ptp": null
                },
                {
                    "family": "AF_INET6",
                    "address": "fe80::7cc0:e649:79b3:dccc",
                    "netmask": null,
                    "broadcast": null,
                    "ptp": null
                }
            ]
        }
    ]
}
```


[返回上一级](../README.md)
