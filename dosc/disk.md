## 磁盘信息接口

### 目录
- [磁盘基本信息](#磁盘基本信息)
- [磁盘分区](#磁盘分区)
- [磁盘IO](#磁盘IO)
- [磁盘完整信息](#磁盘完整信息)

#### 磁盘基本信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/disk
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "partition": [
        {
            "device": "C:\\",
            "percent": 37.1
        },
        {
            "device": "D:\\",
            "percent": 59
        },
        {
            "device": "E:\\",
            "percent": 86.4
        },
        {
            "device": "F:\\",
            "percent": 69.6
        },
        {
            "device": "G:\\",
            "percent": 51.5
        }
    ],
    "io": [
        {
            "drive": "PhysicalDrive0",
            "bytes_read_sec": 2097152,
            "bytes_write_sec": 1048576,
            "count_read_sec": 8,
            "count_write_sec": 1
        },
        {
            "drive": "PhysicalDrive1",
            "bytes_read_sec": 0,
            "bytes_write_sec": 0,
            "count_read_sec": 0,
            "count_write_sec": 0
        }
    ]
}
```

#### 磁盘分区
> 请求示例
```http
GET http://127.0.0.1:5000/system/disk/partition
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
[
    {
        "device": "C:\\",
        "mountpoint": "C:\\",
        "fstype": "NTFS",
        "opts": "rw,fixed",
        "total": 120031539200,
        "used": 43166801920,
        "free": 76864737280,
        "percent": 36
    },
    {
        "device": "D:\\",
        "mountpoint": "D:\\",
        "fstype": "NTFS",
        "opts": "rw,fixed",
        "total": 89137324032,
        "used": 52558286848,
        "free": 36579037184,
        "percent": 59
    },
    {
        "device": "E:\\",
        "mountpoint": "E:\\",
        "fstype": "NTFS",
        "opts": "rw,fixed",
        "total": 131078029312,
        "used": 113246347264,
        "free": 17831682048,
        "percent": 86.4
    },
    {
        "device": "F:\\",
        "mountpoint": "F:\\",
        "fstype": "NTFS",
        "opts": "rw,fixed",
        "total": 149946818560,
        "used": 104350617600,
        "free": 45596200960,
        "percent": 69.6
    },
    {
        "device": "G:\\",
        "mountpoint": "G:\\",
        "fstype": "NTFS",
        "opts": "rw,fixed",
        "total": 129942937600,
        "used": 66940751872,
        "free": 63002185728,
        "percent": 51.5
    }
]
```

#### 磁盘IO
> 请求示例
```http
GET http://127.0.0.1:5000/system/disk/io
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                           |
> 响应示例
```json
[
    {
        "drive": "PhysicalDrive0",
        "read_count": 153746,
        "write_count": 866980,
        "read_bytes": 11352313856,
        "write_bytes": 10643150848,
        "read_time": 139,
        "write_time": 143
    },
    {
        "drive": "PhysicalDrive1",
        "read_count": 607331,
        "write_count": 464271,
        "read_bytes": 4877993984,
        "write_bytes": 10123672576,
        "read_time": 3709,
        "write_time": 1383
    }
]
```

#### 磁盘完整信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/disk/info
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "partition": [
        {
            "device": "C:\\",
            "mountpoint": "C:\\",
            "fstype": "NTFS",
            "opts": "rw,fixed",
            "total": 120031539200,
            "used": 43172855808,
            "free": 76858683392,
            "percent": 36
        },
        {
            "device": "D:\\",
            "mountpoint": "D:\\",
            "fstype": "NTFS",
            "opts": "rw,fixed",
            "total": 89137324032,
            "used": 52558286848,
            "free": 36579037184,
            "percent": 59
        },
        {
            "device": "E:\\",
            "mountpoint": "E:\\",
            "fstype": "NTFS",
            "opts": "rw,fixed",
            "total": 131078029312,
            "used": 113246347264,
            "free": 17831682048,
            "percent": 86.4
        },
        {
            "device": "F:\\",
            "mountpoint": "F:\\",
            "fstype": "NTFS",
            "opts": "rw,fixed",
            "total": 149946818560,
            "used": 104350617600,
            "free": 45596200960,
            "percent": 69.6
        },
        {
            "device": "G:\\",
            "mountpoint": "G:\\",
            "fstype": "NTFS",
            "opts": "rw,fixed",
            "total": 129942937600,
            "used": 66940755968,
            "free": 63002181632,
            "percent": 51.5
        }
    ],
    "io": [
        {
            "drive": "PhysicalDrive0",
            "read_count": 153845,
            "write_count": 867488,
            "read_bytes": 11372285952,
            "write_bytes": 10667358208,
            "read_time": 139,
            "write_time": 145
        },
        {
            "drive": "PhysicalDrive1",
            "read_count": 607331,
            "write_count": 464307,
            "read_bytes": 4877993984,
            "write_bytes": 10124246016,
            "read_time": 3709,
            "write_time": 1383
        }
    ]
}
```


[返回上一级](../README.md)
