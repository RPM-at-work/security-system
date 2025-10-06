import logging

from server.common.logger import setup_logger

log = setup_logger("main_db", logging.INFO)

# Usage Example

if __name__ == "__main__":
    from server.db_server.db_manager import DBManager
    from server.db_server.models import User

    # SQLite Example
    log.info("=== SQLite Example ===")
    db = DBManager("sqlite", database=":memory:")

    # Create tables
    db.create_tables()

    db.add(User(name="x", email="y@z.com"))

    with db.session() as session:
        name = db.get(User, session, name="x").name
        log.info(name)
        assert name == "x"
