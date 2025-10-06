from sqlalchemy import Column, String

# from typing import List
# from typing import Optional
# from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = Column(String(100))

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, email={self.email})"
