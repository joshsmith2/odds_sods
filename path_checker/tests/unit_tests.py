from base import *
import os

class DirTest(GeneralTest):

    def test_can_open_file(self):
        out = path_checker.main(self.in_file, self.out_file)
        self.assertIn('/usr/keep/this/in/', out)

    def test_empty_file_for_input(self):
        empty_in = os.path.join(os.path.dirname(self.in_file), 'empty.txt')
        with open(empty_in, 'w') as f:
            f.write('')
        self.assertRaises(Exception, path_checker.main, (empty_in, self.out_file))
        os.remove(empty_in)

if __name__ == '__main__':
    unittest.main()