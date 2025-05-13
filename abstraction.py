from abc import ABC, abstractmethod

class AbstractCalculator(ABC):
    """
    Abstract base class for calculator operations.
    Enforces implementation of all basic operations in any subclass.
    """

    @abstractmethod
    def _add(self, num1, num2): pass

    @abstractmethod
    def _subtract(self, num1, num2): pass

    @abstractmethod
    def _multiply(self, num1, num2): pass

    @abstractmethod
    def _divide(self, num1, num2): pass
