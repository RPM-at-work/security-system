from server.db_server.db_manager import DBManager
from server.grpc_server.grpc_main_server import GRPCServer


class Factory:
    @classmethod
    def create_db_server(cls, dialect, database, **kwargs) -> DBManager:
        return DBManager(dialect=dialect, database=database, **kwargs)

    @classmethod
    def create_grpc_server(cls, host: str, port: int, db: DBManager) -> GRPCServer:
        # create and register servicer
        return GRPCServer(host=host, port=port, db=db)
