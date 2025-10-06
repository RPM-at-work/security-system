from abc import ABC, abstractmethod
from contextlib import contextmanager

import grpc

from server.common.logger import setup_logger
from server.grpc_server.proto import definition_pb2, definition_pb2_grpc

log = setup_logger("API")


class ServerAPIInterface(ABC):
    @abstractmethod
    def say_hello(self, name: str, email: str):
        """gRPC method implementation"""


class ServerAPI(ServerAPIInterface):
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    @contextmanager
    def _grpc_stub(self, stub_class):
        """Context manager for gRPC stub with insecure channel.

        Usage:
            with grpc_stub('localhost', 50051, YourServiceStub) as stub:
                response = stub.YourMethod(request)
        """
        channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        try:
            yield stub_class(channel)
        finally:
            channel.close()

    def say_hello(self, name: str, email: str):
        try:
            with self._grpc_stub(definition_pb2_grpc.GreeterStub) as stub:
                response = stub.SayHello(definition_pb2.HelloRequest(name=name, email=email))
                log.info(f"SayHello response: {response.message}")
                return response.message
        except grpc.RpcError as e:
            err = f"RPC error: {e.__dict__['_state'].code.name}"
            log.error(err)
            raise grpc.RpcError(err) from e


if __name__ == "__main__":
    api = ServerAPI("localhost", 50051)
    api.say_hello("mogozrob2", "domofon2")
