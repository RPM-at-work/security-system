from abc import ABC, abstractmethod
from contextlib import contextmanager

import grpc

from server.grpc_server.proto import definition_pb2, definition_pb2_grpc


class ServerAPIInterface(ABC):
    @abstractmethod
    def say_hello(self):
        """gRPC method implementation"""


class ServerAPI(ServerAPIInterface):
    @contextmanager
    def _grpc_stub(self, host, port, stub_class):
        """Context manager for gRPC stub with insecure channel.

        Usage:
            with grpc_stub('localhost', 50051, YourServiceStub) as stub:
                response = stub.YourMethod(request)
        """
        channel = grpc.insecure_channel(f"{host}:{port}")
        try:
            yield stub_class(channel)
        finally:
            channel.close()

    def say_hello(self):
        with self._grpc_stub("localhost", "50051", definition_pb2_grpc.GreeterStub) as stub:
            response = stub.SayHello(definition_pb2.HelloRequest(name="world"))
            return response.message
