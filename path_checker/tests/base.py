import path_checker
import unittest
import os

class GeneralTest(unittest.TestCase):

    def setUp(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.in_file = os.path.join(current_dir, 'paths.txt')
        self.out_file = os.path.join(current_dir, 'out.txt')

    def tearDown(self):
        if os.path.exists(self.out_file):
            os.remove(self.out_file)

if __name__ == '__main__':
    unittest.main()