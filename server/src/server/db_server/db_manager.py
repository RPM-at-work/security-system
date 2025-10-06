from typing import Any, List, Optional, Type
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

from server.db_server.models import Base


class DBManager:
    """Pythonic database interface using SQLAlchemy"""

    def __init__(self, dialect: str, **config):
        """
        Initialize database connection

        Args:
            dialect: 'sqlite' or 'postgresql'
            **config: Database configuration
                For SQLite: database (path, or ':memory:')
                For PostgreSQL: host, port, database, user, password
        """
        self.engine = self._create_engine(dialect, **config)
        self.SessionFactory = sessionmaker(bind=self.engine)
        self.base = Base

    def _create_engine(self, dialect: str, **config):
        """Create SQLAlchemy engine based on dialect"""
        dialect = dialect.lower()

        if dialect == "sqlite":
            db_path = config.get("database", ":memory:")
            return create_engine(f"sqlite:///{db_path}")

        elif dialect in ("postgresql", "postgres"):
            host = config.get("host", "localhost")
            port = config.get("port", 5432)
            database = config.get("database")
            user = config.get("user")
            password = config.get("password")
            return create_engine(
                f"postgresql://{user}:{password}@{host}:{port}/{database}"
            )

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

    def __del__(self):
        self.drop_tables()

    def create_tables(self):
        """Create all tables defined in models"""
        self.base.metadata.create_all(self.engine)

    def drop_tables(self):
        self.base.metadata.drop_all(self.engine)

    # CRUD Methods
    def add(self, obj):
        """Add a single object"""
        with self.session() as s:
            s.add(obj)

    def add_all(self, objects: List):
        """Add multiple objects"""
        with self.session() as s:
            s.add_all(objects)

    def _get(self, model: Type, session: Session, **filters) -> Optional[Any]:
        """
        Get a single object by filters

        Args:
            model: The model class to query
            session: Session with DB
            **filters: Column name and value pairs to filter by

        Returns:
            First matching object or None

        Example:
            user = db.get(User, id=1)
            user = db.get(User, name='Alice')
        """
        stmt = select(model)
        for key, value in filters.items():
            stmt = stmt.where(getattr(model, key) == value)
        result = session.execute(stmt)
        return result.scalar_one_or_none()

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

    def count(self, model: Type, **filters) -> int:
        """
        Count objects matching filters

        Args:
            model: The model class to query
            **filters: Column name and value pairs to filter by

        Returns:
            Count of matching objects

        Example:
            count = db.count(User)
            count = db.count(User, name='Alice')
        """
        return len(self.get_all(model, **filters))
