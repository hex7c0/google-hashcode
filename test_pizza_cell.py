# -*- coding: utf-8 -*-
"""PizzaCell test."""

import unittest

from pizza_cell import Ingredient, PizzaCell


class PizzaCellTestCase(unittest.TestCase):

    def test_cheese(self):
        with self.assertRaises(ValueError):
            PizzaCell('cheese')

    def test_mushroom(self):
        cell = PizzaCell(Ingredient.MUSHROOM.value)
        self.assertTrue(cell.mushroom)
        self.assertFalse(cell.tomato)

    def test_tomato(self):
        cell = PizzaCell(Ingredient.TOMATO.value)
        self.assertFalse(cell.mushroom)
        self.assertTrue(cell.tomato)


if __name__ == '__main__':
    unittest.main()
