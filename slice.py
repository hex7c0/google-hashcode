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
    :type __id: int
    """

    _cells = []
    _indices = {}

    __index = 0
    __id = 0

    def __init__(self):
        """Slice constructor."""

        self._cells = []
        self._indices = {}
        self.__index = 0
        self.__generate_id()

    def __generate_id(self, cell: Cell = None) -> None:
        """Generate if of this slice.

        :param cell:
        :type cell: Cell
        :return:
        :rtype: None
        """

        default = 0

        if self.__index is default:
            self.__id = default

        if cell is not None:
            self.__id += cell.id

    def __len__(self) -> int:
        """Return length of this slice.

        :return:
        :rtype: int
        """

        return self.__index

    def __add__(self, cell: Cell):
        """Add a cell into list of cells.

        :param cell: single cell
        :type cell: Cell
        :return: this slice
        :rtype: Slice
        """

        try:  # easier to ask for forgiveness than permission
            self._indices[cell.id]
        except KeyError:
            pass
        else:  # duplicated cell
            raise KeyError

        self._cells.append(cell)
        self._indices[cell.id] = self.__index

        self.__index += 1
        self.__generate_id(cell)

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

        self.__id = key if key is self.__index else self._cells[key].id

        return self.__id

    @property
    def cells(self) -> Cells:
        """Return list of cells.

        :return: list of cells
        :rtype: Cells
        """

        return self._cells

    @property
    def id(self) -> int:
        """Return id of this slice.

        :return: id
        :rtype: int
        """

        return self.__id
