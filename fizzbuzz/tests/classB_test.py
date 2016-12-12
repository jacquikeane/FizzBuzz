import unittest
import os
import filecmp
from fizzbuzz import classB

modules_dir = os.path.dirname(os.path.abspath(classB.__file__))
data_dir = os.path.join(modules_dir, 'tests', 'data')

class TestClassB(unittest.TestCase):
    def test_init(self):
        fb = classB.ClassB(42)
        self.assertEqual(fb.max_number, 42)


    def test_is_fizzy(self):
        fb = classB.ClassB()
        tests = [
            (1, False),
            (2, False),
            (3, True),
            (4, False),
            (5, False),
            (6, True),
            (7, False),
            (8, False),
            (9, True),
            (10, False),
        ]

        for number, expected in tests:
            self.assertEqual(expected, fb._is_fizzy(number))


    def test_is_buzzy(self):
        fb = classB.ClassB()
        tests = [
            (1, False),
            (2, False),
            (3, False),
            (4, False),
            (5, True),
            (6, False),
            (7, False),
            (8, False),
            (9, False),
            (10, True),
        ]

        for number, expected in tests:
            self.assertEqual(expected, fb._is_buzzy(number))


    def test_number_to_string(self):
        fb = classB.ClassB()
        tests = [
            (1, '1'),
            (2, '2'),
            (3, 'Fizz'),
            (4, '4'),
            (5, 'Buzz'),
            (6, 'Fizz'),
            (7, '7'),
            (15, 'FizzBuzz'),
        ]



    def test_run(self):
        tmp_file = 'tmp.test.classB.run.out'
        expected_file = os.path.join(data_dir, 'classB_test_run.out')
        fb = classB.ClassB(20)
        fb.run(outfile=tmp_file)
        self.assertTrue(filecmp.cmp(expected_file, tmp_file, shallow=False))
        os.unlink(tmp_file) 

