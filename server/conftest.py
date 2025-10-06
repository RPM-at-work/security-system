## tmp file fixture
## pytest_container or python_on_whales
import pytest

from server.security_server.config import DBServerConfig
from server.security_server.factory import Factory

db_config = DBServerConfig(**{"dialect": "sqlite", "database": "/tmp/tests/app.db"})


@pytest.fixture(scope="module")
def db():
    db = Factory.create_db_server(db_config)
    db.start()
    yield db
    db._drop_tables()
