import pytest
from math import pi

from figure_lib.figure import InputValuesNotLegitException
from figure_lib.circle import Circle


class TestCircle:
    precision = 0.01 # Точность вычислений (на случай, если будут погрешности, например, из-за использования типа float)
    
    # Тест на неверные значения входных данных
    def test_circle_invalid_input_value(self) -> None:
        with pytest.raises(InputValuesNotLegitException):
            circle = Circle(-9) # Нарушение ограничений для входных данных
    
    # Тест на неверный тип входных данных
    def test_circle_invalid_input_value_type(self) -> None:
        with pytest.raises(InputValuesNotLegitException):
            circle = Circle("a") # Неправильный тип входных данных
    
    # Тест на существующий круг с радиусом типа int
    def test_circle_int_input_value(self) -> None:
        circle = Circle(5) # Существующий круг
        assert abs(circle.get_area() - self._circle_area(circle.radius)) < self.precision
    
    # Тест на существующий круг с радиусом типа float
    def test_circle_float_input_value(self) -> None:
        circle = Circle(12.3) # Существующий круг
        assert abs(circle.get_area() - self._circle_area(circle.radius)) < self.precision

    def _circle_area(self, radius: int | float) -> float:
        return pi * radius**2
