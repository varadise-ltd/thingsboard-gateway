import grpc
import asyncio

from thingsboard_gateway.gateway.proto.messages_pb2 import *
import thingsboard_gateway.gateway.proto.messages_pb2_grpc as messages_pb2_grpc


class TBGRPCServer(messages_pb2_grpc.TBGatewayProtoServiceServicer):
    async def read_client_requests(self, request_iter):
        async for client_update in request_iter:
            print("Recieved message from client:", client_update, end="")

    async def write_server_responses(self, context):
        for i in range(15):
            await context.write(FromServiceMessage(dummy_value=str(i)))
            await asyncio.sleep(0.5)

    async def participate(self, request_iter, context):
        read_task = asyncio.create_task(self.read_client_requests(request_iter))
        write_task = asyncio.create_task(self.write_server_responses(context))

        await read_task
        await write_task

async def serve():
    server = grpc.aio.server()

    # game_pb2_grpc.add_GameServicer_to_server(Game(), server)
    server.add_insecure_port("[::]:9595")
    await server.start()
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())