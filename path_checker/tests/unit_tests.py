from base import *
import os

class DirTest(GeneralTest):

    def test_empty_file_for_input_raises_exception(self):
        empty_in = os.path.join(os.path.dirname(self.in_file), 'empty.txt')
        with open(empty_in, 'w') as f:
            f.write('')
        self.assertRaises(Exception, path_checker.main, (empty_in, self.out_file))
        os.remove(empty_in)

class StandaloneTests(unittest.TestCase):

    def test_can_compare_lists(self):
        empty = []
        short = ['bum', 'bag', 'ting']
        long = ['bum', 'bag', 'ting', 'pang']
        differs = ['pin','pun','ping']
        last_differs = ['bum', 'bag', 'tinge']
        self.assertTrue(path_checker.lists_equal_to_length_of_shortest(empty, long))
        self.assertTrue(path_checker.lists_equal_to_length_of_shortest(short, long))
        self.assertTrue(path_checker.lists_equal_to_length_of_shortest(long, short))
        self.assertFalse(path_checker.lists_equal_to_length_of_shortest(short, differs))
        self.assertFalse(path_checker.lists_equal_to_length_of_shortest(short, last_differs))

    def test_comparison_is_agnostic_about_lists_with_empty_members(self):
        short = ['', 'bag', 'ting']
        long = ['', 'bag', 'ting','tang']
        trailing_spaces = ['', 'bag', 'ting', '', '', '']
        mid_space = ['','bag','','ting', 'tang']
        self.assertTrue(path_checker.lists_equal_to_length_of_shortest(short, long))
        self.assertTrue(path_checker.lists_equal_to_length_of_shortest(short, trailing_spaces))
        self.assertTrue(path_checker.lists_equal_to_length_of_shortest(short, mid_space))


if __name__ == '__main__':
    unittest.main()