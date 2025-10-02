from server.db_server.interface import DBInterface
from server.grpc.server import GRPCServer


class Factory:


    def create_db_server(self) -> DBInterface:
        # return DBServer()
        pass

    def create_grpc_server(self) -> GRPCServer:
        pass
