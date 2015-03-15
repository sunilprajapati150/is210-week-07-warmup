#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03."""


# Import Python libs
import decimal
import unittest

# Import User libs
import data
import task_03


class Task03TestCase(unittest.TestCase):
    """Test cases for Task 03"""

    def test_to_analyze_required(self):
        """Tests that to_analyze is a required argument"""
        with self.assertRaises(TypeError):
            task_03.lexicographics()

    def test_lexicographics(self):
        """Tests that lexicographics returns the correct values."""
        expected = (12, 5, decimal.Decimal(407) / 50)
        returned = task_03.lexicographics(data.SHAKESPEARE)
        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()
