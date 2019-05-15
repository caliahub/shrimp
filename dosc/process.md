## 内存信息接口

### 目录
- [进程基本信息](#进程基本信息)
- [单进程信息](#单进程信息)
- [单进程参数信息](#单进程参数信息)
- [进程完整信息](#进程完整信息)

#### 进程基本信息
返回消耗内存最大的10（默认）条进程信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/process
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|num|否|数字|返回数目（默认10）                                                                                                          |
> 响应示例
```json
[
    {
        "pid": 4436,
        "name": "eclipse.exe",
        "username": "PC-201807062037\\Administrator",
        "cpu_percent": 0,
        "memory_percent": 5.805025852813063,
        "num_openfiles": 149,
        "num_threads": 53
    },
    {
        "pid": 4328,
        "name": "pycharm64.exe",
        "username": "PC-201807062037\\Administrator",
        "cpu_percent": 0,
        "memory_percent": 15.417995032147495,
        "num_openfiles": 111,
        "num_threads": 62
    }
]
```

#### 单进程信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/process/<pid>/<info>
```
|路径名称|必须|类型|说明|
|:---:|:---:|:---:|:---:|
|\<pid>|是|数字|进程ID|
|\<info>|是|字符串|查询项名称|

|查询项名称|说明|
|:---:|:---:|
|is_running|进程是否存在|
|ppid|进程父PID|
|name|进程名称|
|exe|该进程执行绝对路径|
|cmdline|执行命令|
|environ|环境变量|
|create_time|创建时间|
|parent|父进程|
|status|进程状态|
|cwd|进程当前工作目录|
|username|拥有该进程用户的名称|
|nice|进程优先级|
|ionice|进程IO优先级|
|io_counters|进程IO统计信息|
|num_ctx_switches|上下文切换次数|
|num_handles|句柄数|
|num_threads|线程数|
|threads|相关线程|
|cpu_percent|CPU频率|
|memory_info|内存信息|
|open_files|进程所打开的文件|
|connections|套接字连接|
|is_running|进程是否存在|

> 响应示例
```json
[
    {
        "fd": -1,
        "family": 2,
        "type": 1,
        "laddr": [
            "192.168.0.83",
            51402
        ],
        "raddr": [
            "52.27.199.167",
            80
        ],
        "status": "CLOSE_WAIT"
    }
]
```

#### 单进程参数信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/process/<pid>
```
|路径名称|必须|类型|说明|
|:---:|:---:|:---:|:---:|
|\<pid>|是|数字|进程ID|

|参数名称|必须|类型|说明|
|:---:|:---:|:---:|:---:|
|simple|否|布尔（true/false）|是否查询简略信息，默认true                                                                                                          |
> 响应示例
```json
[
    {
        "name": "chrome.exe",
        "username": "PC-201807062037\\Administrator",
        "pid": 9980
    },
    {
        "name": "firefox.exe",
        "username": "PC-201807062037\\Administrator",
        "pid": 9992
    }
]
```

#### 进程完整信息
> 请求示例
```http
GET http://127.0.0.1:5000/system/process/info
```
|参数名称|必须|类型|说明                                                                                                                 |
|:---:|:---:|:---:|:---:|
|simple|否|布尔（true/false）|是否查询简略信息，默认true                                                                                                          |
> 响应示例
```json
[
    {
        "name": "chrome.exe",
        "username": "PC-201807062037\\Administrator",
        "pid": 9980
    },
    {
        "name": "firefox.exe",
        "username": "PC-201807062037\\Administrator",
        "pid": 9992
    }
]
```
或
```json
[
    {
        "nice": 32,
        "ionice": 2,
        "name": "chrome.exe",
        "io_counters": [38901, 82688, 106540028, 75426876, 665, 4778],
        "cmdline": ["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", "--type=renderer", "--field-trial-handle=1380,13887453687483051265,12329424540744213141,131072", "--service-pipe-token=11369085740279188398", "--lang=zh-CN", "--disable-client-side-phishing-detection", "--enable-offline-auto-reload", "--enable-offline-auto-reload-visible-only", "--device-scale-factor=1", "--num-raster-threads=2", "--enable-main-frame-before-activation", "--service-request-channel-token=11369085740279188398", "--renderer-client-id=605", "--no-v8-untrusted-code-mitigations", "--mojo-platform-channel-handle=3176", "/prefetch:1"],
        "connections": [],
        "pid": 10080,
        "username": "PC-201807062037\\Administrator",
        "create_time": 1554196017.0,
        "memory_maps": [
            ["C:\\Windows\\System32\\locale.nls", 421888],
            ["C:\\Windows\\System32\\oleaccrc.dll", 4096],
            ["C:\\Program Files (x86)\\Google\\Chrome\\Application\\73.0.3683.86\\v8_context_snapshot.bin", 692224],
            ["C:\\Program Files (x86)\\Google\\Chrome\\Application\\73.0.3683.86\\natives_blob.bin", 86016],
            ["C:\\Program Files (x86)\\Google\\Chrome\\Application\\73.0.3683.86\\Locales\\zh-CN.pak", 233472],
            ["C:\\Program Files (x86)\\Google\\Chrome\\Application\\73.0.3683.86\\chrome_100_percent.pak", 888832],
            ["C:\\Windows\\System32\\apisetschema.dll", 4096]
        ],
        "memory_percent": 1.006276254111184,
        "memory_full_info": null,
        "cpu_affinity": [0, 1, 2, 3],
        "cwd": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\73.0.3683.86",
        "environ": {
            "ALLUSERSPROFILE": "C:\\ProgramData",
            "APPDATA": "C:\\Users\\Administrator\\AppData\\Roaming",
            "CHROME_CRASHPAD_PIPE_NAME": "\\\\.\\pipe\\crashpad_2852_XREZISCWMBRFMBKK",
            "WINDOWS_TRACING_LOGFILE": "C:\\BVTBin\\Tests\\installpackage\\csilogfile.log"
        },
        "num_handles": 337,
        "num_threads": 17,
        "threads": [
            [2960, 43.2434772, 1.8564119],
            [5380, 0.0, 0.0],
            [10044, 0.031200199999999997, 0.015600099999999999],
            [6792, 0.0, 0.0],
            [7000, 0.0, 0.0],
            [9520, 0.0, 0.0]
        ],
        "cpu_percent": 0.0,
        "num_ctx_switches": [503365, 0],
        "open_files": [
            ["C:\\Windows\\Fonts\\DejaVuSansMono-Oblique_0.ttf", -1],
            ["C:\\Windows\\Fonts\\ARIALNBI.TTF", -1],
            ["C:\\Program Files (x86)\\Google\\Chrome\\Application\\73.0.3683.86\\chrome_100_percent.pak", -1],
            ["C:\\Program Files (x86)\\Google\\Chrome\\Application\\73.0.3683.86\\natives_blob.bin", -1],
            ["C:\\Windows\\Fonts\\courbi.ttf", -1],
            ["C:\\Program Files (x86)\\Google\\Chrome\\Application\\73.0.3683.86\\chrome_200_percent.pak", -1],
            ["C:\\Windows\\Fonts\\cour.ttf", -1]
        ],
        "status": "running",
        "exe": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
        "cpu_times": [55.130753399999996, 3.900025, 0.0, 0.0],
        "ppid": 2852,
        "memory_info": [84992000, 77352960, 526075, 182906880, 84992000, 774496, 767216, 47280, 34696, 77352960, 174989312, 77352960]
    }
]
```

[返回上一级](../README.md)
