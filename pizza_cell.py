# -*- coding: utf-8 -*-
"""PizzaCell class."""

from enum import Enum, unique

from cell import Cell
from slice import Slice


@unique
class Ingredient(Enum):
    """Ingredient enum."""
    
    MUSHROOM = 'M'
    TOMATO = 'T'


class PizzaCell(object):
    """Cell of Pizza.

    :type ingredient: Ingredient or None
    :type top: PizzaCell or None
    :type bottom: PizzaCell or None
    :type right: PizzaCell or None
    :type left: PizzaCell or None
    :type _cell: Cell or None
    :type _slice: Slice or None
    :type _has_mushroom: bool
    """

    ingredient = None

    top = None
    bottom = None
    right = None
    left = None

    _slice = None
    _cell = None

    _has_mushroom = False

    def __init__(self, ingredient: str):
        """PizzaCell constructor.

        :param ingredient: ingredient in the cell
        :type ingredient: str
        """

        try:
            ingredient = ingredient.upper()
        except AttributeError:
            raise ValueError

        if ingredient == Ingredient.MUSHROOM.value:
            self.ingredient = Ingredient.MUSHROOM
            self._has_mushroom = True
        elif ingredient == Ingredient.TOMATO.value:
            self.ingredient = Ingredient.TOMATO
        else:
            raise ValueError

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

        return not self._has_mushroom

    @property
    def x(self) -> int:
        """Return X of this cell.

        :return: x
        :rtype: int
        """

        return self._cell.x

    @property
    def y(self) -> int:
        """Return Y of this cell.

        :return: y
        :rtype: int
        """

        return self._cell.y

    @property
    def id(self) -> int:
        """Return id of this cell.

        :return: id
        :rtype: int
        """

        return self._cell.id

    def set_neighbour(self, direction: str, next_pizza_cell) -> None:
        """Look at next cell.

        :param direction: direction of the next cell
        :param next_pizza_cell: next PizzaCell
        :param direction: str
        :type next_pizza_cell: PizzaCell
        :return:
        :rtype: None
        """

        setattr(self, direction, next_pizza_cell)

    def is_equal(self, cell) -> bool:
        """Check if cell is equal.

        :param cell: different PizzaCell
        :type cell: PizzaCell
        :return:
        :rtype: bool
        """

        return self.ingredient == cell.ingredient
