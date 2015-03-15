#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02."""


# Import Python libs
import unittest

# Import User libs
import task_02


class Task02TestCase(unittest.TestCase):
    """Test cases for Task 02"""

    def test_bval_required(self):
        """Tests that bval is a required argument"""
        with self.assertRaises(TypeError):
            task_02.bool_to_str()

    def test_bool_to_str(self):
        """Tests that bool_to_str() returns the correct values."""
        testmap = [
            (True, 'Yes'),
            (False, 'No'),
            ([1, 2, 3], 'Yes'),
            ((), 'No'),
            ('abracadabra', 'Yes'),
            ('', 'No')
        ]

        msg = 'Tried bool_to_str() with value {}, expected {}'
        for testval, expected in testmap:
            failmsg = msg.format(testval, expected)
            self.assertEqual(task_02.bool_to_str(testval), expected, failmsg)


if __name__ == '__main__':
    unittest.main()
