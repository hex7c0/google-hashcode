# -*- coding: utf-8 -*-
"""Pizza test."""

import unittest
from os import unlink

from main import read_input
from pizza_cell import Ingredient

input_file = 'test.in'
input_text = b'''3 5 1 6
TTTTT
TMMMT
TTTTT
'''


class PizzaTestCase(unittest.TestCase):
    pizza = None

    def setUp(self):
        """setUp test.

        :return:
        """

        super(PizzaTestCase, self).setUp()
        
        try:
            unlink(input_file)
        except FileNotFoundError:
            pass

        with open(input_file, 'wb') as file_descriptor:
            file_descriptor.write(input_text)

        self.pizza = read_input(input_file)

    def tearDown(self):
        """tearDown test.

        :return:
        """

        try:
            unlink(input_file)
        except FileNotFoundError:
            pass

        super(PizzaTestCase, self).tearDown()

    def test_pizza_cons(self):
        self.assertIsNotNone(self.pizza)
        self.assertEqual(3, self.pizza.rows)
        self.assertEqual(5, self.pizza.columns)
        self.assertEqual(1, self.pizza.minimum_ingredient_number)
        self.assertEqual(6, self.pizza.maximum_cells_number)
        self.assertEqual(3, self.pizza.number_of_mushrooms)
        self.assertEqual(12, self.pizza.number_of_tomatoes)
        self.assertEqual(15, self.pizza.number_of_ingredients)

    def test_pizza_cell(self):
        pizza_cell = self.pizza.cells[0][0]
        self.assertFalse(pizza_cell.mushroom)
        self.assertTrue(pizza_cell.tomato)
        self.assertEqual(Ingredient.TOMATO, pizza_cell.ingredient)

        cell = pizza_cell.cell
        self.assertEqual(0, cell.x)
        self.assertEqual(0, cell.y)
        self.assertEqual(0, cell.id)
        self.assertFalse(cell.is_equal)

        pizza_cell = self.pizza.cells[0][1]
        self.assertFalse(pizza_cell.mushroom)
        self.assertTrue(pizza_cell.tomato)
        self.assertEqual(Ingredient.TOMATO, pizza_cell.ingredient)

        cell = pizza_cell.cell
        self.assertEqual(1, cell.x)
        self.assertEqual(0, cell.y)
        self.assertEqual(10, cell.id)
        self.assertFalse(cell.is_equal)

    @unittest.skip('debug only')
    def test_pizza_print(self):
        self.pizza.print()

    def test_pizza_neighbour(self):
        self.pizza.map()

        # top-left
        pizza_cell = self.pizza.cells[0][0]
        self.assertIsNone(pizza_cell.top)
        self.assertIsNone(pizza_cell.left)
        self.assertTrue(pizza_cell.bottom.is_equal)
        self.assertTrue(pizza_cell.right.is_equal)
        self.assertEqual(0, pizza_cell.bottom.x)
        self.assertEqual(1, pizza_cell.bottom.y)
        self.assertEqual(1, pizza_cell.right.x)
        self.assertEqual(0, pizza_cell.right.y)

        # bottom-left
        pizza_cell = self.pizza.cells[2][0]
        self.assertTrue(pizza_cell.top.is_equal)
        self.assertIsNone(pizza_cell.left)
        self.assertIsNone(pizza_cell.bottom)
        self.assertTrue(pizza_cell.right.is_equal)
        self.assertEqual(0, pizza_cell.top.x)
        self.assertEqual(1, pizza_cell.top.y)
        self.assertEqual(1, pizza_cell.right.x)
        self.assertEqual(2, pizza_cell.right.y)

        # first-mushroom
        pizza_cell = self.pizza.cells[1][1]
        self.assertFalse(pizza_cell.top.is_equal)
        self.assertFalse(pizza_cell.left.is_equal)
        self.assertFalse(pizza_cell.bottom.is_equal)
        self.assertTrue(pizza_cell.right.is_equal)


if __name__ == '__main__':
    unittest.main()
