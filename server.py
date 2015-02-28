#encoding=utf8
import re
import sys
import string
import getopt
import logging
import msgfilter_pb2
import autoMachine
from gevent import server
from gevent.server import _tcp_listener
from gevent.server import _udp_socket
from gevent.monkey import patch_all; patch_all()
from multiprocessing import Process, current_process, cpu_count


global ac_machine

logger = logging.getLogger('server_log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')  

notice_log = logging.FileHandler('msg.log')
notice_log.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(notice_log)


'''
构建自动机
'''
def build_tree(filename):
    global ac_machine
    ac_machine = autoMachine.UnicodeAcAutomation()
    with open(filename, 'r') as fp:
        for one in fp.readlines():
            ac_machine.insert(one.strip().decode('utf8'))

    ac_machine.build_automation()

'''
    删除标点符号和数字
'''
def delStr(buff):
    delEStr = string.punctuation + ' ' + string.digits 
    buff = buff.translate(string.maketrans('', ''), delEStr)
    '''
    delCStr = '＜＞｛｝［］（）％￥＃＠！＆×＾《》&%￥#@！{}【】'
    buff = buff.translate(string.maketrans('', ''), delCStr)
    '''
    return buff

def filterCallback(socket, address):
    global ac_machine
    try:
        buf = socket.recv(2048)
    except Exception,e:
        logger.warning("recv_req error:" + str(e))
        return
    if len(buf) == 0:
        logger.warning('recv msg empty!')
        return 
    msg_req = msgfilter_pb2.MsgFilterRequest()
    try:
        msg_req.ParseFromString(buf)
    except Exception, e:
        logger.warning('parse request error: ' + str(e))
        return
    msg = delStr(msg_req.msg.encode('utf8'))
    ret = ac_machine.matchOne(msg.decode('utf8'))
    ret = ret[0]
    logger.info("msg:%s ret:%s" % (msg_req.msg, ret))
    resp = msgfilter_pb2.MsgFilterResponse(error_code = 0, desc = 'success', ret = ret)
    socket.sendall(resp.SerializeToString())
    socket.close()
def serve_forever(listener):
    server.StreamServer(listener, filterCallback).serve_forever()

def usage():
    print >> sys.stderr, "Options and arguments (and corresponding environment variables):\n\
            --dict : The key dict file default key_dict.txt\n\
            --port : The bind port default 8080\n\
            --cpu : The Process num, default 4\n\
            --help : print usage\n"

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], '',["help", "dict=", "port=", "cpu="])
    except Exception as Exc:
        usage()
        sys.exit(0)
    dict_file = "key_dict.txt"
    port = 8080
    process_num = 4
    for opt, val in opts:
        if opt == "--help":
            usage()
            sys.exit(0)
        if opt == "--dict":
            dict_file = val
        if opt == "--cpu":
            process_num = int(val)
        if opt == "--port":
            port = int(val)
    build_tree(dict_file)
    listener = _tcp_listener(('127.0.0.1', port))
    #listener = _udp_socket(('127.0.0.1', port))
    for i in xrange(process_num):
        Process(target = serve_forever, args = (listener, )).start()
    serve_forever(listener)
