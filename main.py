#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""Pizza problem:

one line containing the following natural numbers separated by single spaces:
* R​ (1 ≤ R ≤ 1000) ​is the number of rows,
* C​ (1 ≤ C ≤ 1000) is the number of columns,
* L​ (1 ≤ L ≤ 1000) ​is the minimum number of each ingredient cells in a slice,
* H​ (1 ≤ H ≤ 1000) ​is the maximum total number of cells of a slice
"""

from os.path import isfile
from sys import argv

from cell import Cell
from pizza import Pizza
from pizza_cell import PizzaCell

HEADERS_SEPARATOR = ' '
HEADERS_NUMBER = 4
HEADERS_MAX = 1000
HEADERS_MIN = 1


def read_input(file_name: str = '') -> Pizza:
    """Read input from file and compile a pizza.

    :param file_name: optional file name
    :type file_name: str
    :return: compiled pizza
    :rtype: Pizza
    :raises FileNotFoundError: if file missing or is not valid
    :raises ValueError: if file input is wrong or malformed
    """

    pizza = None

    try:
        file_name = file_name if file_name else argv[1]
    except IndexError:
        raise FileNotFoundError
    else:
        if not isfile(file_name):
            raise FileNotFoundError

    with open(file_name) as file_descriptor:
        headers_line = file_descriptor.readline()
        if not headers_line:
            raise ValueError

        headers = headers_line.split(HEADERS_SEPARATOR, HEADERS_NUMBER - 1)
        headers = map(int, headers)
        headers = map(lambda value: min(value, HEADERS_MAX), headers)
        headers = map(lambda value: max(value, HEADERS_MIN), headers)
        headers = list(headers)

        try:
            rows = headers[0]
            columns = headers[1]
            minimum_ingredient_number = headers[2]
            maximum_cells_number = headers[3]
        except IndexError:
            raise ValueError

        cells = [[None for _ in range(columns)] for _ in range(rows)]

        number_of_mushrooms = 0
        number_of_tomatoes = 0

        for row in range(rows):
            for column in range(columns):
                cell = Cell(column, row)
                pizza_cell = PizzaCell(str(file_descriptor.read(1)))
                pizza_cell.cell = cell

                cells[row][column] = pizza_cell
                number_of_mushrooms += 1 if pizza_cell.mushroom else 0
                number_of_tomatoes += 1 if pizza_cell.tomato else 0
            file_descriptor.read(1)

        pizza = Pizza(cells)
        pizza.rows = rows
        pizza.columns = columns
        pizza.minimum_ingredient_number = minimum_ingredient_number
        pizza.maximum_cells_number = maximum_cells_number
        pizza.number_of_mushrooms = number_of_mushrooms
        pizza.number_of_tomatoes = number_of_tomatoes

    return pizza


if __name__ == '__main__':
    read_input()
