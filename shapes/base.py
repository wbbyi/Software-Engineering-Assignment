from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def parameters(self) -> dict:
        """返回绘图所需的参数"""
        pass
