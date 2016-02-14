# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        list=[1,1,2,6,24,120,720,5040,40320,362880,3628800]
        for i in range(10):
            self.assertEqual(utils.fact(i),list[i])
        with self.assertRaises(ValueError):
            utils.fact(-1)
        with self.assertRaises(TypeError):
            utils.fact('a')

    def test_roots(self):
        with self.assertRaises(TypeError):
            utils.roots('a',2,4)
        self.assertEqual(utils.roots(0,4,4),tuple(-1))
        self.assertEqual(utils.roots(0,4,0),tuple(0))
        self.assertEqual(utils.roots(0,0,4),tuple())


    
    def test_integrate(self):
        self.assertEqual(utils.integrate('3',0,3),9)
        with self.assertRaises(TypeError):
            utils.integrate('x^2','a',4)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())

