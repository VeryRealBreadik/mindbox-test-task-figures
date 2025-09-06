from figure_lib.figure import Figure, FigureNotLegitException


class Triangle(Figure):
    def __init__(self, side1: int | float, side2: int | float, side3: int | float):
        super().__init__(side1, side2, side3)
        self.sides = [side1, side2, side3]
        self._check_figure_legit()
        self.area = self._calculate_area()
    
    def is_right_triangle(self) -> bool:
        longest_side = max(self.sides)
        longest_side_index = self.sides.index(longest_side)
        remaining_sides = self.sides[:longest_side_index] + self.sides[longest_side_index + 1:]
        return longest_side**2 == sum(map(lambda side: side**2, remaining_sides))
    
    def _check_figure_legit(self) -> None:
        sides_sum = sum(self.sides)
        for side in self.sides:
            if sides_sum - side <= side:
                raise self._figure_not_legit_exception()
    
    def _figure_not_legit_exception(self) -> Exception:
        return FigureNotLegitException("Треугольник с такими вводными данными не может существовать")
    
    def _calculate_area(self) -> float:
        perimeter = sum(self.sides) / 2
        return (perimeter * (perimeter - self.sides[0]) * (perimeter - self.sides[1]) \
                     * (perimeter - self.sides[2]))**0.5
