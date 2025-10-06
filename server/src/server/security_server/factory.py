from server.db_server.db_manager import DBManager
from server.grpc_server.grpc_main_server import GRPCServer
from server.security_server.config import DBServerConfig


class Factory:
    @classmethod
    def create_db_server(cls, config: DBServerConfig) -> DBManager:
        return DBManager(config)

    @classmethod
    def create_grpc_server(cls, host: str, port: int) -> GRPCServer:
        # create and register servicer
        return GRPCServer(host=host, port=port)
