from abc import ABC, abstractmethod


class CameraInterface(ABC):

    @abstractmethod
    def connect(self):
        """connect to camera"""

    @abstractmethod
    def disconnect(self):
        """disconnect from camera"""
