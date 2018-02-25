# -*- coding: utf-8 -*-
"""PizzaSlice test."""

import unittest

from cell import Cell
from pizza_cell import Ingredient, PizzaCell
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

        pizza_cell = PizzaCell(Ingredient.MUSHROOM.value)

        self.cell0 = Cell(X0, Y0)
        self.cell1 = Cell(X1, Y1)

        self.slice0 = Slice()
        pizza_cell.cell = self.slice0
        self.slice0 += pizza_cell

        self.slice1 = Slice()
        pizza_cell.cell = self.slice1
        self.slice1 += pizza_cell
        
        self.pizza_slice = PizzaSlice()

    def test_slice_key(self):
        pizza_cell = PizzaCell(Ingredient.MUSHROOM.value)

        pizza_cell.cell = self.slice0
        self.pizza_slice += pizza_cell
        self.assertEqual(0, self.pizza_slice[self.slice0.id])
        self.assertEqual(1, len(self.pizza_slice.slices))

        pizza_cell.cell = self.slice1
        with self.assertRaises(KeyError):
            self.pizza_slice += pizza_cell

        with self.assertRaises(KeyError):
            if self.pizza_slice['foobar']:
                pass



if __name__ == '__main__':
    unittest.main()
