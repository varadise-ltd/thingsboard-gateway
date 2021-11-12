import asyncio
import grpc
from time import sleep

from thingsboard_gateway.gateway.proto.messages_pb2_grpc import add_TBGatewayProtoServiceServicer_to_server
from thingsboard_gateway.gateway.grpc_service.tb_grpc_server import TBGRPCServer


class TBGRPCServerManager():
    def __init__(self, config):
        self.stopped = False
        self.__config = config
        self.__grpc_port = config['serverPort']
        self.__connectors_sessions = {}
        self.__grpc_server = TBGRPCServer(self.read_cb, self.write_cb)
        asyncio.run(self.serve(), debug=True)
        while not self.stopped:
            sleep(.1)

    def write_cb(self):
        pass

    def read_cb(self, msg):
        self.write("","")
        pass

    def write(self, connector_name, data):
        # if self.__connectors_sessions.get(connector_name) is not None:
            self.__grpc_server.write(self.__grpc_server.get_response('SUCCESS'))

    async def serve(self):
        self.__aio_server = grpc.aio.server()
        add_TBGatewayProtoServiceServicer_to_server(self.__grpc_server, self.__aio_server)
        self.__aio_server.add_insecure_port("[::]:%s"%(self.__grpc_port,))
        await self.__aio_server.start()
        await self.__aio_server.wait_for_termination()

    def stop(self):
        self.stopped = True
        self.__aio_server.stop()


if __name__ == '__main__':
    test_conf = {"serverPort":9595}
    TBGRPCServerManager(test_conf)
