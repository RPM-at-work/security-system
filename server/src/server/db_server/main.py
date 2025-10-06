import logging

from server.common.logger import setup_logger
from server.db_server.db_manager import DBManager
from server.db_server.models import User

log = setup_logger("main_db", logging.INFO)

# Usage Example

if __name__ == "__main__":
    # SQLite Example
    log.info("=== SQLite Example ===")
    db = DBManager(dialect="sqlite", database="app.db")

    # Create tables
    db.start()

    db.add(User(name="xYZ", email="y@z.com"))

    name = db.get(User).name
    log.info(name)
    assert name == "xYZ"
