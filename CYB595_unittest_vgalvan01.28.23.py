import unittest

class TestCase(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hello world'.upper(), 'HELLO WORLD')


if __name__ == '__main__':
    unittest.main()

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hello world'.upper(), 'HELLO WORLD')

    def test_isupper(self):
        self.assertTrue('HELLO WORLD'.isupper())
        self.assertFalse('hello world'.isupper())

    def test_split(self):
        s = 'helloworld'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()