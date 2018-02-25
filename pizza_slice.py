# -*- coding: utf-8 -*-
"""PizzaSlice class."""

from typing import List

from pizza_cell import PizzaCell
from slice import Slice

__all__ = ('PizzaSlice',)

Slices = List[Slice]


class PizzaSlice(object):
    """PizzaSlice is an aggregate of Slice.

    :type _slices: Slices
    :type _indices: dict
    :type __index: int
    """

    _slices = []
    _indices = {}

    __index = 0

    def __init__(self):
        """PizzaSlice constructor."""

        self._slices = []
        self._indices = {}
        self.__index = 0

    def __add__(self, slice: Slice):
        """Add a slice into list of slices.

        :param slice: single slice
        :type slice: Slice
        :return:
        :rtype: None
        """

        try:  # easier to ask for forgiveness than permission
            self._indices[slice.id]
        except KeyError:
            pass
        else:  # duplicated cell
            raise KeyError

        self._slices.append(slice)
        self._indices[slice.id] = self.__index

        self.__index += 1

        return self

    def __getitem__(self, slice_id) -> Slice:
        """Cell getter.

        :param slice_id: slice id
        :param slice_id: str
        :return: slice
        :rtype: Slice
        """

        return self._indices[slice_id]

    @property
    def slices(self) -> Slices:
        """Return list of slices.

        :return: list of slices
        :rtype: Slices
        """

        return self._slices

    def get_new_slice(self, pizza_cell: PizzaCell) -> Slice:
        """Return new slice with this cell.

        :param pizza_cell: add this cell into new slice
        :type pizza_cell: PizzaCell
        :return: last slice
        :rtype: Slice
        """

        slice = Slice(pizza_cell)

        self.__add__(slice)

        return slice
