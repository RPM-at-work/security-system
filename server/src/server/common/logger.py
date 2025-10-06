import logging


class Logger:
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

    def setup(self):
        # Console handler
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "[%(asctime)s][%(name)s][%(levelname)s]: %(message)s",
            datefmt="%Y.%m.%d %H:%M",
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        self.logger.debug(message)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def warning(self, message: str) -> None:
        self.logger.warning(message)

    def error(self, message: str, exc_info: bool = False) -> None:
        self.logger.error(message, exc_info=exc_info)

    def critical(self, message: str) -> None:
        self.logger.critical(message)


def setup_logger(name: str, level: int = logging.INFO) -> Logger:
    logger = Logger(name, level)
    logger.setup()
    return logger
