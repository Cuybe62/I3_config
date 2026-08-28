from abc import ABC, abstractmethod


class Feature(ABC):

    name = ""
    title = ""
    description = ""

    @abstractmethod
    def create_window(self):
        pass