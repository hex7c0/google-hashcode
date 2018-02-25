# -*- coding: utf-8 -*-
"""Slice class."""

from typing import List

from cell import Cell

__all__ = ('Slice',)

Cells = List[Cell]


class Slice(object):
    """Slice is an aggregate of Cell.

    :type mushroom_number: int
    :type tomato_number: int
    :type cells_number: int
    :type _cells: Cells
    :type _indices: dict
    :type __index: int
    :type __id: int
    """

    mushroom_number = 0
    tomato_number = 0
    cells_number = 0

    _cells = []
    _indices = {}

    __index = 0
    __id = 0

    def __init__(self, cell=None):
        """Slice constructor.

        :param cell: add this cell into new slice
        :type cell: PizzaCell
        """

        self.mushroom_number = 0
        self.tomato_number = 0
        self.cells_number = 0
        self._cells = []
        self._indices = {}
        self.__index = 0
        if cell is not None:
            self.__add__(cell)

    def __len__(self) -> int:
        """Return length of this slice.

        :return:
        :rtype: int
        """

        return self.__index

    def __add__(self, cell):
        """Add a cell into list of cells.

        :param cell: single cell
        :type cell: PizzaCell
        :return: this slice
        :rtype: Slice
        """

        try:  # easier to ask for forgiveness than permission
            self._indices[cell.id]
        except KeyError:
            pass
        else:  # duplicated cell
            raise KeyError

        self._cells.append(cell.cell)
        self._indices[cell.id] = self.__index

        cell.slice = self
        if cell.mushroom:
            self.mushroom_number += 1
        elif cell.tomato:
            self.tomato_number += 1

        self.__index += 1
        self.__generate_id()

        return self

    def __getitem__(self, cell_id) -> Cell:
        """Cell getter.

        :param cell_id: cell id
        :param cell_id: str
        :return: cell
        :rtype: Cell
        """

        return self._indices[cell_id]

    def __hash__(self) -> int:
        """Return id of this slice.

        :return: id
        :rtype: int
        """

        return self.__id

    @property
    def cells(self) -> Cells:
        """Return list of cells.

        :return: list of cells
        :rtype: Cells
        """

        return self._cells

    @property
    def ingredient_number(self) -> int:
        """Get ingredients number.

        :return: number of ingredients
        :rtype: int
        """

        return self.mushroom_number + self.tomato_number

    @property
    def id(self) -> int:
        """Return id of this slice.

        :return: id
        :rtype: int
        """

        return self.__id

    def __generate_id(self) -> None:
        """Generate if of this slice (1° Cell).

        :return:
        :rtype: None
        """

        default = 0

        if self.__index > default:
            self.__id = self._cells[default].id
