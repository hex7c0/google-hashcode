# -*- coding: utf-8 -*-
"""Cell class."""

__all__ = ('Cell',)


class Cell(object):
    """Cell is a point in a map.

    :type x: int
    :type y: int
    :type _is_equal: bool
    """

    x = 0
    y = 0

    _is_equal = False

    def __init__(self, x: int, y: int):
        """Cell constructor.

        :param x: row
        :param y: column
        :type x: int
        :type y: int
        """

        self.x = x
        self.y = y

    def __hash__(self) -> int:
        """Return id of this cell.

        :return: id
        :rtype: int
        """

        return self.x * 10 + self.y

    @property
    def id(self) -> int:
        """Return id of this cell.

        :return: id
        :rtype: int
        """

        return self.__hash__()

    @property
    def is_equal(self) -> bool:
        """IsEqual getter.

        :return: bool
        :rtype: bool
        """

        return self._is_equal

    @is_equal.setter
    def is_equal(self, equal: bool) -> None:
        """IsEqual setter.

        :param equal: is_equal
        :type equal: bool
        :return:
        :rtype: None
        """

        self._is_equal = equal
