# -*- coding: utf-8 -*-
"""Cell class."""

__all__ = ('Cell',)


class Cell(object):
    """Cell is a point in a map.

    :type _x: int
    :type _y: int
    :type _is_equal: bool
    :type __id: int
    """

    _x = 0
    _y = 0
    _is_equal = False

    __id = 0

    def __init__(self, x: int, y: int):
        """Cell constructor.

        :param x: row
        :param y: column
        :type x: int
        :type y: int
        """

        self._x = x
        self._y = y
        self._is_equal = False
        self.__generate_id()

    def __generate_id(self) -> None:
        """Generate if of this cell.

        :return:
        :rtype: None
        """

        self.__id = self.x * 10 + self.y + 1

    def __hash__(self) -> int:
        """Return id of this cell.

        :return: id
        :rtype: int
        """

        return self.__id

    @property
    def x(self) -> int:
        """Return X of this cell.

        :return: x
        :rtype: int
        """

        return self._x

    @x.setter
    def x(self, value: int) -> None:
        """X setter.

        :param value: value
        :type value: int
        :return:
        :rtype: None
        """

        self._x = value
        self.__hash__()

    @property
    def y(self) -> int:
        """Return Y of this cell.

        :return: y
        :rtype: int
        """

        return self._y

    @x.setter
    def x(self, value: int) -> None:
        """Y setter.

        :param value: value
        :type value: int
        :return:
        :rtype: None
        """

        self._y = value
        self.__hash__()

    @property
    def is_equal(self) -> bool:
        """IsEqual getter.

        :return: bool
        :rtype: bool
        """

        return self._is_equal

    @is_equal.setter
    def is_equal(self, value: bool) -> None:
        """IsEqual setter.

        :param value: is_equal
        :type value: bool
        :return:
        :rtype: None
        """

        self._is_equal = value

    @property
    def id(self) -> int:
        """Return id of this cell.

        :return: id
        :rtype: int
        """

        return self.__id
