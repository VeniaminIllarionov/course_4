from abc import ABC, abstractmethod


class Abstr_HH(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_url(self):
        pass
    @abstractmethod
    def save_info(self) -> str or list:
        pass
