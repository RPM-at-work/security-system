from server.common.logger import setup_logger
from server.grpc_server.proto import definition_pb2, definition_pb2_grpc

log = setup_logger(__name__)

# ruff: noqa: N802


class GRPCServicer(definition_pb2_grpc.GreeterServicer):
    """GRPC Servicer"""

    def SayHello(self, request, context):
        log.info("SayHello called")
        return definition_pb2.HelloReply(message="Hello, %s!" % request.name)
