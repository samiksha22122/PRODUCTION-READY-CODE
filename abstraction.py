from abc import ABC, abstractmethod

class AbstractConverter(ABC):
    @abstractmethod
    def kg_to_lbs(self, weight): pass

    @abstractmethod
    def lbs_to_kg(self, weight): pass
