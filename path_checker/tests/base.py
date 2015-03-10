from path_checker import *

import unittest
import os

class GeneralTest(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.in_file = os.path.join(current_dir, 'paths.txt')
        self.out_file = os.path.join(current_dir, 'out.txt')

class DirTest(GeneralTest):

    def test_can_open_file(self):
        out = main(self.in_file, self.out_file)
        self.assertIn('/usr/keep/this/in/', out)

class FunctionalTest(GeneralTest):




if __name__ == '__main__':
    unittest.main()