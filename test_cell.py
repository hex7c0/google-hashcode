# -*- coding: utf-8 -*-
"""Cell test."""

import unittest

from cell import Cell

X0 = 0
Y0 = 0
X1 = 1
Y1 = 1


class CellTestCase(unittest.TestCase):
    cell = None

    def setUp(self):
        """setUp test.

        :return:
        """

        super(CellTestCase, self).setUp()

        self.cell = Cell(X0, Y0)

    def test_cell_key(self):
        self.assertEqual(X0, self.cell.x)
        self.assertFalse(Y0, self.cell.y)

    def test_cell_id(self):
        self.assertEqual(self.cell.id, hash(self.cell))
        self.assertEqual(1, self.cell.id)


if __name__ == '__main__':
    unittest.main()
