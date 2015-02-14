import msgfilter_pb2
from recall.controller import RpcController
import recall.client

if __name__ == '__main__':
    client = recall.client.RpcClient()
    channel = client.get_tcp_channel('127.0.0.1:12345')
    stub = msgfilter_pb2.MsgFilterService_Stub(channel)

    controller = RpcController()
    for _ in xrange(1000):
        req = msgfilter_pb2.MsgFilterRequest(type = 1, msg = "%d" % (_))
        rsp = stub.MsgMethod(controller, req, None)
