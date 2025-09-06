class Figure:
    def __init__(self, *values: list[int | float]):
        self._check_input_values_legit(*values)
        self.area: float = None
    
    def _check_input_values_legit(self, *values) -> None:
        for value in values:
            if not isinstance(value, (int, float)) or value <= 0:
                raise self._input_values_not_legit_exception()
    
    def _input_values_not_legit_exception(self) -> Exception:
        return InputValuesNotLegitException("Все вводные данные для фигуры должны быть одного из численных типов и положительными")
    
    def _calculate_area(self) -> float:
        pass
    
    def get_area(self) -> float:
        return self.area


class InputValuesNotLegitException(Exception):
    pass


class FigureNotLegitException(Exception):
    pass
