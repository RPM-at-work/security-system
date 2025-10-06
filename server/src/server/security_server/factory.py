from server.db_server.db_manager import DBManager
from server.grpc.server import GRPCServer


class Factory:
    def create_db_server(self) -> DBManager:
        # return DBServer()
        pass

    def create_grpc_server(self) -> GRPCServer:
        pass
