import logging

from server.common.logger import setup_logger
from server.db_server.db_manager import DBManager
from server.db_server.models import User
from server.grpc_server.grpc_main_server import GRPCServer
from server.security_server.config import DBServerConfig, GRPCConfig
from server.security_server.factory import Factory

log = setup_logger(__name__, logging.INFO)

db_config = DBServerConfig(**{"dialect": "sqlite", "database": "test.db"})

grpc_config = GRPCConfig(**{"host": "localhost", "port": 50051})


class TestSecurityServer:
    def test_factory(self):
        assert isinstance(Factory.create_db_server(**db_config.model_dump()), DBManager)
        assert isinstance(Factory.create_grpc_server(**grpc_config.model_dump()), GRPCServer)


class TestDB:
    def test_basic_add(self, db):
        name = "xYZ"
        db.add(User(name=name, email="y@z.com"))

        assert db.get(User).name == name
