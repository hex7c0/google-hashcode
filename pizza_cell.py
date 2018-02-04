# -*- coding: utf-8 -*-
"""PizzaCell class."""

from enum import Enum, unique

from cell import Cell
from slice import Slice


@unique
class Ingredient(Enum):
    MUSHROOM = 'M'
    TOMATO = 'T'


class PizzaCell:
    """Cell of Pizza.

    :type ingredient: Ingredient or None
    :type top: Cell or None
    :type bottom: Cell or None
    :type right: Cell or None
    :type left: Cell or None
    :type _cell: Cell or None
    :type _slice: Slice or None
    :type _has_mushroom: bool
    :type _has_tomato: bool
    """

    ingredient = None

    top = None
    bottom = None
    right = None
    left = None

    _slice = None
    _cell = None

    _has_mushroom = False
    _has_tomato = False

    def __init__(self, ingredient: str):
        """PizzaCell constructor.

        :param ingredient: ingredient in the cell
        :type ingredient: str
        """

        if Ingredient.MUSHROOM.value == ingredient.upper():
            self.ingredient = Ingredient.MUSHROOM
            self._has_mushroom = True
        else:
            self.ingredient = Ingredient.TOMATO
        self._has_tomato = not self._has_mushroom

    @property
    def cell(self) -> Cell:
        """Cell getter.

        :return: cell
        :rtype: Cell
        """

        return self._cell

    @cell.setter
    def cell(self, cell: Cell) -> None:
        """Cell setter.

        :param cell: cell
        :type cell: Cell
        :return:
        :rtype: None
        """

        self._cell = cell

    @property
    def slice(self) -> Slice:
        """Slice getter.

        :return: slice
        :rtype: Slice
        """

        return self._slice

    @slice.setter
    def slice(self, slice: Slice) -> None:
        """Slice setter.

        :param slice: slice
        :type slice: Slice
        :return:
        :rtype: None
        """

        self._slice = slice

    @property
    def mushroom(self) -> bool:
        """This cell has mushroom.

        :return: if mushroom
        :rtype: bool
        """

        return self._has_mushroom

    @property
    def tomato(self) -> bool:
        """This cell has tomato.

        :return: if mushroom
        :rtype: bool
        """

        return self._has_tomato

    def neighbour(self, direction: str, next_pizza_cell) -> None:
        """Look at next cell.

        :param direction: direction of the next cell
        :param next_pizza_cell: next PizzaCell
        :param direction: str
        :type next_pizza_cell: PizzaCell
        :return:
        :rtype: None
        """

        cell = Cell(next_pizza_cell.cell.x, next_pizza_cell.cell.y)
        cell.is_equal = self.ingredient == next_pizza_cell.ingredient

        setattr(self, direction, cell)
