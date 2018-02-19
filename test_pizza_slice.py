# -*- coding: utf-8 -*-
"""PizzaSlice test."""

import unittest

from cell import Cell
from pizza_slice import PizzaSlice
from slice import Slice
from test_cell import X0, X1, Y0, Y1


class PizzaSliceTestCase(unittest.TestCase):
    cell0 = None
    cell1 = None
    slice0 = None
    slice1 = None

    def setUp(self):
        """setUp test.

        :return:
        """

        super(PizzaSliceTestCase, self).setUp()

        self.cell0 = Cell(X0, Y0)
        self.cell1 = Cell(X1, Y1)
        self.slice0 = Slice()
        self.slice0 += self.cell0
        self.slice1 = Slice()
        self.slice1 += self.cell1
        self.pizza_slice = PizzaSlice()

    def test_slice_key(self):
        self.pizza_slice += self.slice0
        self.assertEqual(0, self.pizza_slice[self.slice0.id])
        self.assertEqual(1, len(self.pizza_slice.slices))

        self.pizza_slice += self.slice1
        self.assertEqual(1, self.pizza_slice[self.slice1.id])
        self.assertEqual(2, len(self.pizza_slice.slices))

        with self.assertRaises(KeyError):
            if self.pizza_slice['foobar']:
                pass

        with self.assertRaises(KeyError):
            self.pizza_slice += self.slice0


if __name__ == '__main__':
    unittest.main()
