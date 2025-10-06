from concurrent.futures import ThreadPoolExecutor
from typing import Optional

from grpc import Server, server

from server.grpc_server.proto.definition_pb2_grpc import add_GreeterServicer_to_server
from server.grpc_server.servicer import GRPCServicer


class GRPCServer:
    def __init__(self, host: str, port: int):
        self._thread_pool: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=10, thread_name_prefix="grpc_")
        self._server: Optional[Server] = None
        self._host = host
        self._port = port

    def connect(self):
        self._server = server(thread_pool=self._thread_pool)

    def start(self):
        self.connect()
        self.register_services()

        self._server.add_insecure_port(f"{self._host}:{self._port}")
        self._server.start()
        self._server.wait_for_termination()

    def stop(self):
        self._server.stop(grace=10)

    def register_services(self):
        add_GreeterServicer_to_server(GRPCServicer(), self._server)
