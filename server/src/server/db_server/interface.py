from abc import abstractmethod, ABC


class DBInterface(ABC):
    """
    abstract interface for DB interaction {sqlite, postgres, ...}
    """
    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        """Connect to the database."""
