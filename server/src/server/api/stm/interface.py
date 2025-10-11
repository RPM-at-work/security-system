from abc import ABC, abstractmethod


class STMInterface(ABC):
    @abstractmethod
    def connect(self):
        """connect to board"""

    @abstractmethod
    def disconnect(self):
        """disconnect from board"""
