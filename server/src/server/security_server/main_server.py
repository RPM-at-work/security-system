import logging
import signal

from server.common.logger import setup_logger
from server.security_server.config import DBServerConfig, DBServerConfigPostgres, GRPCConfig
from server.security_server.factory import Factory

log = setup_logger("security-system", logging.INFO)

# TODO: move all prod configs to outside yaml file

sqlite_config_model = DBServerConfig(
    **{
        "dialect": "sqlite",
        "database": "/tmp/security-tmp-db.db",
    }
)

postgres_config_model = DBServerConfigPostgres(
    **{
        "dialect": "postgresql",
        "user": "ps_user",
        "password": "dome_pwd_1$",  # TODO: move out + add new user
        "host": "node01.dome",
        "port": 32100,
        "database": "ps_db",
    }
    # NodePort in k8s, instead if internal port its mapped - 5432:32100
)

grpc_config_model = GRPCConfig(
    **{
        "host": "localhost",
        "port": 50051,
    }
)


class SecurityServer:
    def __init__(self):
        log.info("Initializing security server")
        self.db_server = Factory.create_db_server(postgres_config_model)
        self.grpc_server = Factory.create_grpc_server(host=grpc_config_model.host, port=grpc_config_model.port)
        self.grpc_server.register_services(database=self.db_server)

        signal.signal(signal.SIGINT, self.intercept_signals)

    def start(self):
        # init sequence
        log.info("Starting DB server")
        self.db_server.start()
        log.info("Starting GRPC server")
        self.grpc_server.start()

    def stop(self):
        # stop sequence
        log.info("Stopping GRPC server")
        self.grpc_server.stop()

        log.info("Server has stopped!")

    def intercept_signals(self, sig, frame):
        log.warning(f"Caught signal: {sig}")
        self.stop()
        exit(sig)


def main():
    server = SecurityServer()
    server.start()


if __name__ == "__main__":
    main()
    # server is running, stop with ctrl-c, send SIGINT, stop Pycharm
