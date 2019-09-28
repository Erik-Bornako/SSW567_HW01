"""
Author: Erik Bornako
Date: 29 Aug 2019
Purpose: Specifies a triangle
"""

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

    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
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
    
def runClassifyTriangle(a, b, c):
    """ invoke classify_triangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")