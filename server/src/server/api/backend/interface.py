from abc import abstractmethod, ABC


class ServerAPI(ABC):
    @abstractmethod
    def sanity_check(self):
        """gRPC method implementation"""