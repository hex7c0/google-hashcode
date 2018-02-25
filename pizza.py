# -*- coding: utf-8 -*-
"""Pizza class."""

from typing import List

from pizza_cell import PizzaCell
from pizza_slice import PizzaSlice

PizzaCells = List[List[PizzaCell]]


class Pizza:
    """Pizza main class.

    :type rows: int
    :type columns: int
    :type minimum_ingredient_number: int
    :type maximum_cells_number: int
    :type number_of_mushrooms: int
    :type number_of_tomatoes: int
    :type _cells: List[List[PizzaCell]]
    :type _slices: PizzaSlice
    :type _latest_slice: Slice
    """

    rows = 0
    columns = 0
    minimum_ingredient_number = 0
    maximum_cells_number = 0
    number_of_mushrooms = 0
    number_of_tomatoes = 0

    _cells = [[]]
    _slices = None
    _latest_slice = None

    def __init__(self, cells: PizzaCells):
        """Compile a pizza with _cells.

        :param cells: cell with ingredient
        :type cells: List[List[PizzaCell]]
        """

        self._cells = cells
        self._slices = PizzaSlice()

    @property
    def cells(self) -> PizzaCells:
        """Cells getter.

        :return: slices
        :rtype: PizzaCells
        """

        return self._cells

    @property
    def number_of_ingredients(self) -> int:
        """Sum mushrooms and tomatoes.

        :return: sum
        :rtype: int
        """

        return self.number_of_mushrooms + self.number_of_tomatoes

    def map(self) -> None:
        """Map pizza with neighbours.

        :return:
        :rtype: None
        """

        for row in range(self.rows):
            for column in range(self.columns):
                pizza_cell = self._cells[row][column]

                if row != 0:
                    top_pizza_cell = self._cells[row - 1][column]
                    pizza_cell.set_neighbour('top', top_pizza_cell)

                if column != 0:
                    left_pizza_cell = self._cells[row][column - 1]
                    pizza_cell.set_neighbour('left', left_pizza_cell)

                try:
                    bottom_pizza_cell = self._cells[row + 1][column]
                    pizza_cell.set_neighbour('bottom', bottom_pizza_cell)
                except IndexError:
                    pass

                try:
                    right_pizza_cell = self._cells[row][column + 1]
                    pizza_cell.set_neighbour('right', right_pizza_cell)
                except IndexError:
                    pass

    def reduce(self) -> None:
        """Map pizza to big cells.

        :return:
        :rtype: None
        """

        # start = self._cells[row][column]

        for row in range(self.rows):
            for column in range(self.columns):
                cell = self._cells[row][column]
                slice = self._latest_slice

                # first or latest iteraction
                if slice is None or \
                        slice.cells_number > self.maximum_cells_number:
                    self._latest_slice = self._slices.get_new_slice(cell)

                slice = self._latest_slice

                # already assigned
                if cell.slice is not None:
                    continue

                if cell.bottom is not None and cell.bottom.slice is not None:
                    slice += cell

                # cell.used = self._latest_slice

    def print(self) -> None:
        """Print pizza as input.

        :return:
        :rtype: None
        """

        for row in range(self.rows):
            for column in range(self.columns):
                print(self._cells[row][column].ingredient, end=' ')
            print()
