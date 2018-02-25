# -*- coding: utf-8 -*-
"""Slice test."""

import unittest

from cell import Cell
from pizza_cell import Ingredient, PizzaCell
from slice import Slice
from test_cell import X0, X1, Y0, Y1


class SliceTestCase(unittest.TestCase):
    cell0 = None
    cell1 = None
    slice = None

    def setUp(self):
        """setUp test.

        :return:
        """

        super(SliceTestCase, self).setUp()

        self.cell0 = Cell(X0, Y0)
        self.cell1 = Cell(X1, Y1)
        self.slice = Slice()

    def test_slice_key(self):
        pizza_cell = PizzaCell(Ingredient.TOMATO.value)

        pizza_cell.cell = self.cell1
        self.slice += pizza_cell
        self.assertEqual(0, self.slice[self.cell1.id], 'list index of id 1')
        self.assertEqual(1, len(self.slice.cells))

        pizza_cell.cell = self.cell0
        self.slice += pizza_cell
        self.assertEqual(1, self.slice[self.cell0.id], 'list index of id 0')
        self.assertEqual(2, len(self.slice.cells))

        with self.assertRaises(KeyError):
            if self.slice['foobar']:
                pass

        with self.assertRaises(KeyError):
            self.slice += self.cell0

    def test_slice_id(self):
        self.assertEqual(self.slice.id, hash(self.slice))
        self.assertEqual(0, self.slice.id, 'no element')

        pizza_cell = PizzaCell(Ingredient.TOMATO.value)

        pizza_cell.cell = self.cell1
        self.slice += pizza_cell
        self.assertEqual(self.cell1.id, self.slice.id, 'first element')
        self.assertEqual(12, self.slice.id, 'first element')

        pizza_cell.cell = self.cell0
        self.slice += pizza_cell
        self.assertEqual(12, self.slice.id, 'first')


if __name__ == '__main__':
    unittest.main()
