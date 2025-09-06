import pytest

from figure_lib.figure import InputValuesNotLegitException, FigureNotLegitException
from figure_lib.triangle import Triangle


class TestTriangle:
    precision = 0.01 # Точность вычислений (на случай, если будут погрешности, например, из-за использования типа float)
    
    # Тест на неверные значения входных данных
    def test_triangle_invalid_input_value(self) -> None:
        with pytest.raises(InputValuesNotLegitException):
            triangle = Triangle(-3, -4, -5) # Нарушение ограничений для входных данных
    
    # Тест на неверный тип входных данных
    def test_triangle_invalid_input_value_type(self) -> None:
        with pytest.raises(InputValuesNotLegitException):
            triangle = Triangle("1", "3", "3") # Неправильный тип входных данных
    
    # Тест на несуществующий треугольник
    def test_triangle_figure_not_legit(self) -> None:
        with pytest.raises(FigureNotLegitException):
            triangle = Triangle(1, 2, 3) # Несуществующий треугольник
    
    # Тест на существующий не прямоугольный треугольник
    def test_triangle_legit_non_right_triangle(self) -> None:
        triangle = Triangle(5, 5, 8) # Существующий треугольник
        assert abs(triangle.get_area() - self._triangle_area(triangle.sides)) < self.precision
        assert not triangle.is_right_triangle()
    
    # Тест на прямоугольный треугольник
    def test_triangle_legit_right_triangle(self) -> None:
        triangle = Triangle(3, 4, 5) # Прямоугольный треугольник
        assert abs(triangle.get_area() - self._triangle_area(triangle.sides)) < self.precision
        assert triangle.is_right_triangle()

    # Вспомогательный метод для вычисления площади треугольника (на случай, если в классе Triangle указана неправильная формула площади по трём сторонам)
    def _triangle_area(self, sides: list[int | float]) -> float:
        perimeter = sum(sides) / 2
        return (perimeter * (perimeter - sides[0]) * (perimeter - sides[1])  * (perimeter - sides[2]))**0.5
