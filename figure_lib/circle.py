from math import pi

from figure_lib.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int | float):
        super().__init__(radius)
        self.radius = radius
        self.area = self._calculate_area()
    
    def _calculate_area(self) -> float:
        return pi * self.radius**2
