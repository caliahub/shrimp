## 系统信息接口

### 目录
- [基本信息](#基本信息)
- [启动时间](#启动时间)
- [平台信息](#平台信息)
- [登录用户](#登录用户)

#### 基本监控信息
> 请求示例
```http
GET http://127.0.0.1:5000/system
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "boot_time": "2019-04-01 08:31:36",
    "platform": {
        "system": "Windows",
        "release": "7",
        "version": "6.1.7601",
        "machine": "AMD64",
        "processor": "Intel64 Family 6 Model 58 Stepping 9, GenuineIntel",
        "hostname":"PC-201807062037",
        "ip":"192.168.0.83"
    },
    "login_users": [
        {
            "name": "Administrator",
            "termianl": null,
            "host": "0.0.0.0",
            "started": "2019-04-01 08:31:42",
            "pid": null
        }
    ]
}
```

#### 启动时间
> 请求示例
```http
GET http://127.0.0.1:5000/system/boot_time
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "boot_time": "2019-04-01 08:31:36"
}
```

#### 平台信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/platform
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "system": "Windows",
    "release": "7",
    "version": "6.1.7601",
    "machine": "AMD64",
    "processor": "Intel64 Family 6 Model 58 Stepping 9, GenuineIntel",
    "hostname":"PC-201807062037",
    "ip":"192.168.0.83"
}
```

#### 登录用户
> 请求示例
```http
GET http://127.0.0.1:5000/system/login_users
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
[
    {
        "name": "Administrator",
        "termianl": null,
        "host": "0.0.0.0",
        "started": "2019-04-01 08:31:42",
        "pid": null
    }
]
```

[返回上一级](../README.md)
