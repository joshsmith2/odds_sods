from base import *
import os

class DirTest(GeneralTest):

    def test_can_open_file(self):
        out = path_checker.main(self.in_file, self.out_file)
        self.assertIn('/usr/keep/this/in/', out)

if __name__ == '__main__':
    unittest.main()