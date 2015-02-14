import ahocorasick
import thread
import msgfilter_pb2
from recall.server import RpcServer

class MsgFilterServiceImpl(msgfilter_pb2.MsgFilterService):
    def MsgMethod(self, rpc_controller, request, done):
        #print 'recv', request.data
        return msgfilter_pb2.MsgFilterResponse(error_code = 0, desc = "ok", ret = 0)

if __name__ == '__main__':
    addr = ('127.0.0.1', 12345)
    print 'server listen at %s' % str(addr)
    server = RpcServer(addr)
    server.register_service(MsgFilterServiceImpl())
    server.run()

