"""
Author: Erik Bornako
Date: 29 Aug 2019
Purpose: Specifies a triangle
"""

import unittest
import math

def isclose(a, b, rel_tol=1e-06, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def testNumber(number):
    """Tests to see if number is valid"""

    try:
        int(number)
    except ValueError:
        return 'Invalid'
    return 'Valid'

def classify_triangle(a,b,c):
    """Returns the type of triangle"""

    if testNumber(a) == 'Invalid' or testNumber(b) == 'Invalid' or testNumber(c) == 'Invalid':
        return 'NotATriangle'
    
    if a <= 0 or b <= 0 or c <= 0:
        return 'NotATriangle'

    if isclose((a**2 + b**2), c**2) or isclose((a**2 + c**2), b**2) or isclose((b**2 + c**2), a**2):
        right = ' and Right'
    else:
        right = ''

    if a == b and a == c and b == c:
        return 'Equilateral' + right
    
    if (a == b and a != c and b != c) or (a != b and a == c and b != c) or (a != b and a != c and b == c):
        return 'Isosceles' + right
    
    if (a != b and a != c and b != c):
        return 'Scalene' + right
    
    else:
        return 'NotATriangle'
    
def runClassifyTriangle(a, b, c):
    """ invoke classify_triangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")

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
        self.assertEqual(classify_triangle(3,3,20), 'Isosceles')
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