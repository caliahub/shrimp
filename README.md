# shrimp

### 项目描述
轻量级监控数据采集器，用于采集服务器节点信息，支持传输到kafka管道供消费者消费以及支持存储到elasticsearch。

### 特点
- 轻量级
- 支持linux、windows
- RESTful风格API，用于获取即时数据
- kafka存储
- elasticsearch存储

### 配置说明
service.properties

|参数名称|必须|说明|
|:---|:---:|:---|
|server.ip|是|服务IP|
|server.port|是|监听端口|
|kafka|是|是否开启kafka转存（on/off）|
|kafka.bootstrap.servers|否|kafka连接地址|
|kafka.collect.freq|否|采集频率，默认30秒|
|kafka.topic.system|否|system主题名称（默认shrimp-system，不建议修改）|
|elasticsearch|是|是否开启elasticsearch转存（on/off）|
|elasticsearch.hosts|否|elasticsearch连接地址|
|elasticsearch.collect.freq|否|采集频率，默认30秒|
|elasticsearch.index.system|否|system索引名称（默认shrimp-system，不建议修改）|


### 接口
- [系统信息接口](dosc/system.md)：获取系统基础信息
- [CPU信息接口](dosc/cpu.md)：获取系统CPU相关信息
- [内存信息接口](dosc/memory.md)：获取系统内存相关信息
- [磁盘信息接口](dosc/disk.md)：获取系统磁盘相关信息
- [网络信息接口](dosc/network.md)：获取系统网络相关信息
- [进程信息接口](dosc/process.md)：获取系统进程相关信息
