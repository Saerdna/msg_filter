# msg_filter
a rpc server to filter msg

依赖库:protobuf, gevent, python2.7.4+

TCP 连接: 调用样例见 demo.php

server 启动: python server.py

python server.py --dict=dict.txt --port=8080 --cpu=4

dict:指定生效词典的文件

port:指定端口

cpu:指定占用的核数量

匹配关键词使用的是 自动机算法,复杂度 O(MN)

