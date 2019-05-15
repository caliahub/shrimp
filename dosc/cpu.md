## CPU信息接口

### 目录
- [CPU基本信息](#CPU基本信息)
- [CPU时间](#CPU时间)
- [CPU使用率](#CPU使用率)
- [CPU核数](#CPU核数)
- [CPU统计信息](#CPU统计信息)
- [CPU频率](#CPU频率)
- [CPU完整信息](#CPU完整信息)

#### CPU基本信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/cpu
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "percent": 37.5
}
```

#### CPU时间
> 请求示例
```http
GET http://127.0.0.1:5000/system/cpu/time
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "user": 130057.40969599999,
    "system": 6612.180385500018,
    "idle": 337542.951723,
    "interrupt": 186.34319449999998,
    "dpc": 120.90077500000001
}
```

#### CPU使用率
> 请求示例
```http
GET http://127.0.0.1:5000/system/cpu/percent
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|percpu|否|布尔（true/false）|每核CPU使用率 ，默认false                                                                                                       |
> 响应示例
```json
{
    "percent": 50
}
```
或
```json
{
    "percent": [
        50,
        83.3,
        33.3,
        16.7
    ]
}
```

#### CPU核数
> 请求示例
```http
GET http://127.0.0.1:5000/system/cpu/count
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|logical|否|布尔（true/false）|是否逻辑核数 ，默认true                                                                                                      |
> 响应示例
```json
{
    "count": 4
}
```
或
```json
{
    "count": 2
}
```

#### CPU统计信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/cpu/stats
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|无|否|无|无                                                                                                          |
> 响应示例
```json
{
    "ctx_switches": 3291928849,
    "interrupts": 1073866372,
    "soft_interrupts": 0,
    "syscalls": 219512348
}
```

#### CPU频率
> 请求示例
```http
GET http://127.0.0.1:5000/system/cpu/freq
```
|参数名称|必须|类型|说明|
|:---:|:---:|:---:|:---:|
|percpu|否|布尔（true/false）|每核CPU频率 ，默认false |
> 响应示例
```json
{
    "current": 3201,
    "min": 0,
    "max": 3201
}
```
或
```json
[
    {
        "current": 3201,
        "min": 0,
        "max": 3201
    },
    {
        "current": 3164,
        "min": 0,
        "max": 3164
    },
    {
        "current": 3245,
        "min": 0,
        "max": 3245
    },
    {
        "current": 3051,
        "min": 0,
        "max": 3051
    }
]
```

#### CPU完整信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/cpu/info
```
|参数名称|必须|类型|说明                                                                                                            
|:---:|:---:|:---:|:---:|
|percpu|否|布尔（true/false）|每核CPU频率 ，默认false|                                                                                    
|logical|否|布尔（true/false）|是否逻辑核数 ，默认true | 
> 响应示例
```json
{
    "time": {
        "user": 131342.1715316,
        "system": 6667.077137399989,
        "idle": 340734.2485799,
        "interrupt": 188.1684062,
        "dpc": 122.35158429999998
    },
    "percent": 42.9,
    "count": 4,
    "stats": {
        "ctx_switches": 3305997127,
        "interrupts": 1077945698,
        "soft_interrupts": 0,
        "syscalls": 238135244
    },
    "freq": {
        "current": 3201,
        "min": 0,
        "max": 3201
    }
}
```

[返回上一级](../README.md)
