import sys
from gevent import server
from gevent.server import _tcp_listener
from gevent.monkey import patch_all; patch_all()
from multiprocessing import Process, current_process, cpu_count
 
def note(format, *args):
    sys.stderr.write('[%s]\t%s\n' % (current_process().name, format%args))
 
def echo(socket, address):
    #print 'New connection from %s:%s' % address
    socket.recv(1024)
    socket.sendall('HTTP/1.1 200 OK\n\nHello World!!')
    socket.close()
    '''
    fileobj = socket.makefile()
    fileobj.write('Welcome to the echo server! Type quit to exit.\r\n')
    fileobj.write('In %s\r\n' % current_process().name)
    fileobj.flush()
    while True:
        line = fileobj.readline()
        if not line:
            print "client disconnected"
            break
        if line.strip().lower() == 'quit':
            print "client quit"
            break
        fileobj.write(current_process().name + '\t' + line)
        fileobj.flush()
        print "echoed", repr(line)
    '''
 
listener = _tcp_listener(('127.0.0.1', 8002))
 
def serve_forever(listener):
    note('starting server')
    server.StreamServer(listener, echo).serve_forever()
     
number_of_processes = 1
print 'Starting %s processes' % number_of_processes
for i in range(number_of_processes):
    Process(target=serve_forever, args=(listener,)).start()
 
serve_forever(listener)

