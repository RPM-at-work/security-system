from server.db_server.db_manager import DBManager
from server.grpc_server.server import GRPCServer


class Factory:
    @classmethod
    def create_db_server(cls, dialect, **kwargs) -> DBManager:
        return DBManager(dialect=dialect, **kwargs)

    @classmethod
    def create_grpc_server(cls) -> GRPCServer:
        # create and register servicer
        return GRPCServer()
