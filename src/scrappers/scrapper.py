from abc import ABC, abstractmethod

class Scrapper(ABC):
    def __init__(self, source):
        self.source = source

    @abstractmethod
    def extract_calls(self):
        pass