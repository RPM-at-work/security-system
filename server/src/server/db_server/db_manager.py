from contextlib import contextmanager
from typing import List, Type

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from server.common.logger import setup_logger
from server.db_server.dto import BaseTDO
from server.db_server.models import Base
from server.security_server.config import DBServerConfig

log = setup_logger(__name__)


class DBManager:
    """Pythonic database interface using SQLAlchemy"""

    def __init__(self, config: DBServerConfig):
        """
        Initialize database connection

        Args:
            dialect: 'sqlite' or 'postgresql'
            **config: Database configuration
                For SQLite: database (path, or ':memory:')
                For PostgreSQL: host, port, database, user, password
        """
        self._config = config
        self.engine = self._create_engine()
        self.SessionFactory = None

    def start(self):
        self.create_tables()
        self.SessionFactory = sessionmaker(bind=self.engine)

    def _create_engine(self):
        """Create SQLAlchemy engine based on dialect"""
        dialect = self._config.dialect

        if dialect == "sqlite":
            db_path = self._config.database
            if not db_path:
                return create_engine("sqlite://")
            return create_engine(f"sqlite:///{db_path}")

        elif dialect in ("postgresql", "postgres"):
            host = self._config.host
            port = self._config.port
            db_path = self._config.database
            user = self._config.user
            password = self._config.password
            return create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_path}")

        else:
            raise ValueError(f"Unsupported dialect: {dialect}")

    @contextmanager
    def session(self):
        """Context manager for database sessions"""
        session = self.SessionFactory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_tables(self):
        """Create all tables defined in models"""
        Base.metadata.create_all(self.engine)

    def _drop_tables(self):
        Base.metadata.drop_all(self.engine)

    # CRUD Methods
    def add(self, obj):
        """Add a single object"""
        with self.session() as s:
            s.add(obj)

    def add_all(self, objects: List):
        """Add multiple objects"""
        with self.session() as s:
            s.add_all(objects)

    def get(self, model: Type) -> BaseTDO:
        """
        Get a single object by filters

        Args:
            model: The model class to query

        Returns:
            First matching object or None

        Example:
            user = db.get(User, id=1)
            user = db.get(User, name='Alice')
        """
        with self.session() as s:
            stmt = select(model)
            result = s.execute(stmt)
            db_res = result.scalar_one()
            return BaseTDO(name=db_res.name, email=db_res.email)

    def update(self, obj):
        """Update an existing object"""
        with self.session() as s:
            s.merge(obj)

    def delete(self, obj):
        """Delete an object"""
        with self.session() as s:
            s.delete(obj)

    def delete_by_filter(self, model: Type, **filters):
        """
        Delete objects matching filters

        Args:
            model: The model class to query
            **filters: Column name and value pairs to filter by

        Example:
            db.delete_by_filter(User, name='Alice')
        """
        with self.session() as s:
            stmt = select(model)
            for key, value in filters.items():
                stmt = stmt.where(getattr(model, key) == value)
            result = s.execute(stmt)
            objects = result.scalars().all()
            for obj in objects:
                s.delete(obj)
