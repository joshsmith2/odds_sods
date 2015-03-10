from base import *

class OutputTrimmedPaths(GeneralTest):

    def test_the_whole_process(self):
        path_checker.main(self.in_file, self.out_file)

        expected = ['/usr/take/out/but/keep/this', '/usr/keep.txt',
                    '/usr/still/in']
        unexpected = ['/usr/', '', '/usr/take/out']

        with open(self.out_file, 'r') as out_f:
            lines = [l.strip for l in out_f.readlines()]

        self.assertEqual(set(lines), set(expected))

if __name__ == '__main__':
     unittest.main()