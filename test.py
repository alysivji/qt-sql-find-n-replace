"""Tests for SQL Find and Replacer

how to run: python test.py
"""

import unittest
import app

class SQLReplacerTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_find_n_replacer(self):
        self.assertEqual("SELECT * FROM Table1", \
                         app.SQLReplacer.sql_query_find_n_replace(self, \
                                                                  "SELECT * FROM Table0", \
                                                                  ['Table0'], ['Table1']))

if __name__ == '__main__':
    unittest.main()
