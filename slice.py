# -*- coding: utf-8 -*-
"""Slice class."""

from typing import List

from cell import Cell

__all__ = ('Slice',)

Cells = List[Cell]


class Slice(object):
    """Slice is an aggregate of Cell.

    :type _cells: Cells
    :type _indices: dict
    :type __index: int
    """

    _cells = []
    _indices = {}

    __index = 0

    def __init__(self):
        """Slice constructor."""

        self._cells = []
        self._indices = {}
        self.__index = 0

    def __add__(self, cell: Cell):
        """Add a cell into list of cells.

        :param cell: single cell
        :type cell: Cell
        :return:
        :rtype: None
        """

        # duplicated cell
        if cell.id in self._indices:
            raise KeyError

        self._cells.append(cell)
        self._indices[cell.id] = self.__index

        self.__index += 1

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

        key = 0

        return key if key is self.__index else self._cells[key].id

    @property
    def id(self) -> int:
        """Return id of this slice.

        :return: id
        :rtype: int
        """

        return self.__hash__()

    @property
    def cells(self) -> Cells:
        """Return list of cells.

        :return: list of cells
        :rtype: Cells
        """

        return self._cells
