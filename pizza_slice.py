# -*- coding: utf-8 -*-
"""PizzaSlice class."""

from slice import Slice

__all__ = ('PizzaSlice',)


class PizzaSlice(object):
    """PizzaSlice is an aggregate of Slice.

    """

    _slices = []
    _indices = {}

    __index = 0

    def __add__(self, slice: Slice):
        """Add a slice into list of slices.

        :param slice: single slice
        :type slice: Slice
        :return:
        :rtype: None
        """

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
