# -*- coding: utf-8 -*-
"""Slice test."""

import unittest

from cell import Cell
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
        self.slice += self.cell1
        self.assertEqual(0, self.slice[self.cell1.id], 'list index of id 1')
        self.assertEqual(1, len(self.slice.cells))

        self.slice += self.cell0
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

        self.slice += self.cell1
        self.assertEqual(self.cell1.id, self.slice.id, 'first element')
        self.assertEqual(11, self.slice.id, 'first element')

        self.slice += self.cell0
        self.assertEqual(11, self.slice.id, 'same because first element')


if __name__ == '__main__':
    unittest.main()
