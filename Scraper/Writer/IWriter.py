from abc import ABC, abstractmethod


class IWriter(ABC):
    @abstractmethod
    def write(self):
        return NotImplemented
