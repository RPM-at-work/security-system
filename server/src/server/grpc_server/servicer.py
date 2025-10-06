from proto import definition_pb2, definition_pb2_grpc


class GRPCServicer(definition_pb2_grpc.GreeterServicer):
    """GRPC Servicer"""

    def SayHello(self, request, context):
        return definition_pb2.HelloReply(message="Hello, %s!" % request.name)
