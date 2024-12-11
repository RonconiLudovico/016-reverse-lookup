import unittest

from main import main, reverseLookup


class Test01(unittest.TestCase):
    def test_main(self):
        '''
        Here we test the main function
        '''
        data = {1 : 'a', 2 : 'b', 3 : 'b', 4 : 'b', 5 : 'c'}
        result = main(data)
        self.assertEqual(([1], [2, 3, 4], []), result)


class Test02(unittest.TestCase):
    def test_reverseLookup(self):
        '''
        Here we test the main function
        '''
        data1 = {1 : 'a', 2 : 'b', 3 : 'b', 4 : 'b', 5 : 'c'}
        data2 = 'a'
        result = reverseLookup(data1, data2)
        self.assertEqual([1], result)

class Test03(unittest.TestCase):
    def test_reverseLookup(self):
        '''
        Here we test the main function
        '''
        data1 = {1 : 'a', 2 : 'b', 3 : 'b', 4 : 'b', 5 : 'c'}
        data2 = 'b'
        result = reverseLookup(data1, data2)
        self.assertEqual([2, 3, 4], result)


class Test04(unittest.TestCase):
    def test_reverseLookup(self):
        '''
        Here we test the main function
        '''
        data1 = {1 : 'a', 2 : 'b', 3 : 'b', 4 : 'b', 5 : 'c'}
        data2 = 'd'
        result = reverseLookup(data1, data2)
        self.assertEqual([], result)
