from server.common.logger import setup_logger
from server.db_server.db_manager import DBManager
from server.db_server.models import User
from server.grpc_server.proto import definition_pb2, definition_pb2_grpc

log = setup_logger(__name__)

# ruff: noqa: N802


class GRPCServicer(definition_pb2_grpc.GreeterServicer):
    """GRPC Servicer"""

    def __init__(self, db: DBManager):
        self.db = db

    def SayHello(self, request, context):
        log.info(f"SayHello called with: {request.name}, adding to DB")
        self.db.add(
            obj=User(
                name=request.name,
                email=request.email,
            )
        )
        return definition_pb2.HelloReply(message="Hello, %s!" % request.name)
