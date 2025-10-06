from concurrent.futures import ThreadPoolExecutor
from typing import Optional

from grpc import Server, server
from proto.definition_pb2_grpc import add_GreeterServicer_to_server
from servicer import GRPCServicer


class GRPCServer:
    def __init__(self):
        self._thread_pool: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=10, thread_name_prefix="grpc_")
        self._server: Optional[Server] = None

    def connect(self):
        self._server = server(thread_pool=self._thread_pool)

    def start(self):
        self.register_services()

        self._server.add_insecure_port("[::]:50051")
        self._server.start()
        self._server.wait_for_termination()

    def register_services(self):
        add_GreeterServicer_to_server(GRPCServicer(), self._server)
