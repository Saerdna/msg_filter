import ahocorasick
import msgfilter_pb2
import logging
from gevent import server
from gevent.server import _tcp_listener
from gevent.monkey import patch_all; patch_all()
from multiprocessing import Process, current_process, cpu_count
global ac_machine

def build_tree():
    global ac_machine
    ac_machine = ahocorasick.KeywordTree()
    with open('key_word.txt', 'r') as fp:
        for one in fp.readlines():
            ac_machine.add(one.strip())

    ac_machine.make()

def filterCallback(socket, address):
    global ac_machine
    content = ''
    while True:
        try:
            buf = socket.recv(1024)
        except Exception,e:
            logging.warning("recv_req error:" + str(e))
            break
        if len(buf) == 0:
            break
        content += buf
    if len(content) == 0:
        logging.warning('recv msg empty!')
        return 
    msg_req = msgfilter_pb2.MsgFilterRequest()
    try:
        msg_req.ParseFromString(content)
    except Exception, e:
        logging.warning('parse request error: ' + str(e))
        return
    
    ret = ac_machine.search(msg_req.msg)
    if ret[0] >= len(msg_req.msg):
        ret = False
    else:
        ret = True
    resp = msgfilter_pb2.MsgFilterResponse(error_code = 0, desc = 'success', ret = ret)
    socket.sendall(resp.SerializeToString())
    socket.close()

def serve_forever(listener):
    server.StreamServer(listener, filterCallback).serve_forever()

if __name__ == '__main__':
    build_tree()
    listener = _tcp_listener(('127.0.0.1', 8080))
    number_of_processes = 1
    for i in xrange(number_of_processes - 1):
        Process(target = serve_forever, args = (listener, )).start()
    serve_forever(listener)
