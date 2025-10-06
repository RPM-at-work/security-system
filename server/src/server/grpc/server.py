from concurrent.futures import ThreadPoolExecutor
from typing import Optional

from grpc import server, Server


class GRPCServer:
    def __init__(self):
        self._thread_pool: ThreadPoolExecutor = ThreadPoolExecutor(
            max_workers=10, thread_name_prefix="grpc_"
        )
        self._server: Optional[Server] = None

    def connect(self):
        self._server = server(thread_pool=self._thread_pool)
