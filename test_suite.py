from Erik_Bornako_SSW567_HW01 import classify_triangle, runClassifyTriangle
import unittest
import math

class TestTriangles(unittest.TestCase):

    def testClassifyTriangle(self):
        self.assertEqual(classify_triangle(1,1,1), 'Equilateral')
        self.assertEqual(classify_triangle(0,0,0), 'NotATriangle')
        self.assertEqual(classify_triangle(-3,-4,-5), 'NotATriangle')
        self.assertEqual(classify_triangle(0,0,10), 'NotATriangle')
        self.assertEqual(classify_triangle(10,10,10), 'Equilateral')
        self.assertEqual(classify_triangle(3.0,3,3.000), 'Equilateral')
        self.assertEqual(classify_triangle(3,4,5), 'Scalene and Right')
        self.assertEqual(classify_triangle(3,3,math.sqrt(18)), 'Isosceles and Right')
        self.assertEqual(classify_triangle(3,3,20), 'NotATriangle')
        self.assertEqual(classify_triangle(3,3,'hello'), 'NotATriangle')

if __name__ == '__main__':
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(1,1,1)
    runClassifyTriangle(0,0,0)
    runClassifyTriangle(-3,-4,-5)
    runClassifyTriangle(0,0,10)
    runClassifyTriangle(10,10,10)
    runClassifyTriangle(3.0,3,3.000)
    runClassifyTriangle(3,4,5)
    runClassifyTriangle(3,3,math.sqrt(18))
    runClassifyTriangle(3,3,20)
    runClassifyTriangle(3,3,'hello')

    unittest.main(exit=False, verbosity=2)