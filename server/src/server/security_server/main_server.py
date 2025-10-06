import logging
import signal

from server.common.logger import setup_logger
from server.security_server.config import DBServerConfig, GRPCConfig
from server.security_server.factory import Factory

log = setup_logger("security-system", logging.INFO)

sqlite_config_model = DBServerConfig(
    **{
        "dialect": "sqlite",
        "database": ":memory:",
    }
)

grpc_config_model = GRPCConfig(
    **{
        "host": "localhost",
        "port": 50051,
    }
)


class SecurityServer:
    def __init__(self):
        self.db_server = Factory.create_db_server(dialect=sqlite_config_model.dialect, database=sqlite_config_model.database)
        self.grpc_server = Factory.create_grpc_server(host=grpc_config_model.host, port=grpc_config_model.port)
        signal.signal(signal.SIGINT, self.intercept_signals)
        log.info("Initializing security server")

    def start(self):
        # init sequence
        log.info("Starting DB server")
        self.db_server.start()
        log.info("Starting GRPC server")
        self.grpc_server.start()

    def stop(self):
        # stop sequence
        log.info("Stopping DB server")
        self.grpc_server.stop()

        log.info("Server has stopped!")

    def intercept_signals(self, sig, frame):
        log.warning(f"Caught signal: {sig}")
        self.stop()
        exit(sig)


if __name__ == "__main__":
    ss = SecurityServer()
    ss.start()
