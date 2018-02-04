# -*- coding: utf-8 -*-
"""PizzaSlice class."""

from typing import List

from slice import Slice

__all__ = ('PizzaSlice',)

Slices = List[Slice]


class PizzaSlice(object):
    """PizzaSlice is an aggregate of Slice.

    :type _slices: Cells
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

        # duplicated slice
        if slice.id in self._indices:
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
