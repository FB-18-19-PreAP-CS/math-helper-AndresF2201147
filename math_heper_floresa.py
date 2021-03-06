from math import *
from time import *

'''
5 tests of the 5 formulas here
'''

def equation(x1,y1,x2,y2):
    '''Returns the equation of the line going through points (x1,y1)
       and (x2,y2) in slope intercept form; y = mx + b
       
    >>> equation(3,-2,5,-1)
    'y = 0.5x + -3.5'
    
    >>> equation(10,8,-5,5)
    'y = 0.2x + 6.0'
    
    >>> equation(-10,-15,-15,-20)
    'y = 1.0x + -5.0'

    >>> equation(5.8,9.2,5,4)
    'y = 6.5x + -28.5'
    
    >>> equation(0,0,0,0)
    'x = 0'
    '''
    
    
    if x1 == 0 and y2 == 0 and x2 == 0 and y2 == 0:
        return('x = 0')
    
    slope = (y2 - y1) / (x2 - x1)
    mx = slope * x1
    intercept = y1 - mx
    
    return(f'y = {round(slope,2)}x + {round(intercept,2)}')


def heron(a,b,c):
    '''Returns the area of a triangle given sides a, b, and c
       The three sides must comply with the Triangle Inequality Theorem - The sum of the lengths
       of any two sides of a triangle is greater than the length of the third side.
       
       >>> heron(7,10,9)
       '30.59'
       
       >>> heron(100,135,226)
       '3595.41'
       
       >>> heron(4.4,5.5,7.708000)
       '11.85'
       
       >>> heron(2,7,9)
       Traceback (most recent call last):
        ...
       ValueError: Impossible input due to one side being too small(Triangle Inequality Theorem)
       
       >>> heron(75.3,26.75,9.07)
       Traceback (most recent call last):
        ...
       ValueError: Impossible input due to one side being too small(Triangle Inequality Theorem)
    '''
    if a + b <= c or b + c <= a or a + c <= b:
        raise ValueError("Impossible input due to one side being too small(Triangle Inequality Theorem)")

    
    s = (a + b + c) / 2
    ans = sqrt(s * (s - a) * (s - b) * (s - c))
    
    return(f"{round(ans,2)}")

def quad(a,b,c):
    '''Returns two answers(zeros) using the quadratic formula for a quadratic equation
       Inputing the 'a' value, 'b' value, and 'c' value from
       ax^2 + bx + c = 0
       
       >>> quad(1,6,8)
       (-2.0, -4.0)
       
       >>> quad(1,16,0)
       (0.0, -16.0)
       
       >>> quad(3,-11,-6)
       (4.15, -0.48)
       
       >>> quad(2,1,-6)
       (1.5, -2.0)
       
       >>> quad(0,-50,48)
       Traceback (most recent call last):
        ...
       ValueError: a cannot be 0
    '''
    if a == 0:
        raise ValueError("'a' cannot be 0")
    if ((b**2) - (4 * (a * c))) < 0:
        raise ValueError("Cannot square root a negative integer")
    
    ans1 = -(b) + sqrt((b**2) - (4*(a*c)))
    ans2 = -(b) - sqrt((b**2) - (4*(a*c)))
    
    
    final1 = ans1 / (2 * a)
    final2 = ans2 / (2 * a)
    
    tup = (round(final1,2),round(final2,2))
    return(tup)
    
def pyth(a,b):
    '''Pythagorean Theorem -  the square of the hypotenuse of a right triangle is equal to the sum of the squares
       of the other two sides
       Given 2 sides, this will find the length of the hypotenuse
       a^2 + b^2 = c^2
       
       >>> pyth(4,6)
       '7.21'
       
       >>> pyth(6.6,10.3)
       '12.23'
       
       >>> pyth(23000,63.3)
       '23000.09'
       
       >>> pyth(-12,7)
       Traceback (most recent call last):
        ...
       ValueError: Inputs must be a positive integer
       
       >>> pyth(-4,-15)
       Traceback (most recent call last):
        ...
       ValueError: Inputs must be a positive integer
    '''
    if a < 0 or b < 0:
        raise ValueError("Inputs must be a positive integer")
    
    c = sqrt((a**2) + (b**2))
    
    return(f"{round(c,2)}")

def ask_equation():
    while True:
        print('Give your two points (x1,y1,x2,y2)')
        try:
            x1 = float(input('x1: '))
            y1 = float(input('y1: '))
            x2 = float(input('x2: '))
            y2 = float(input('y2: '))
            print(f"The equation of the line going through points ({x1},{y1}) and ({x2,y2}) is {equation(x1,y1,x2,y2)}")
            break
        except ValueError as e:
            print(f"Error: {e}")

    
def ask_heron():
    while True:
        print('Give your three sides of the triangle (a,b,c)')
        try:
            a = float(input('a: '))
            b = float(input('b: '))
            c = float(input('c: '))
            print(f"The area of a triangle from side {a}, {b}, and {c} is {heron(a,b,c)}")
            break
        except ValueError as e:
            print(f"Error: {e}")

def ask_quad():
    while True:
        print('Give your three inputs (ax^2 + bx + c)')
        try:
            a = float(input('a: '))
            b = float(input('b: '))
            c = float(input('c: '))
            tup = quad(a,b,c)
            print(f"The zeros of the quadratic equation {a}x^2 + {b}x + {c} = 0 is \n {tup[0]} and {tup[1]}")
            break
        except ValueError as e:
            print(f"Error: {e}")

    
def ask_pyth():
    while True:
        print('Give the two measurements of a right triangle to find the hypotenuse - c \n (a,b)')
        try:
            a = float(input('a: '))
            b = float(input('b: '))
            print(f"The hypotenuse of a right triangle with side {a} and {b} is {pyth(a,b)}")
            break
        except ValueError as e:
            print(f"Error: {e}")

        
def main():
    while True:
        print("--Pick an equation to use -- \n (1) Equation of the line going through two points \n (2) Heron's formula (area of triangle) \n (3) Quadratic Formula \n (4) Pythagorean Theorem \n \n If you would like to quit input 'quit'")
        print()
        ans = input('Which one would you like to use?: ')
        
        if ans.lower() == 'quit':
            print()
            break        
        
        elif ans == '1':
            print()
            ask_equation()
            print()
            
        elif ans == '2':
            print()
            ask_heron()
            print()
            
        elif ans == '3':
            print()
            ask_quad()
            print()
            
        elif ans == '4':
            print()
            ask_pyth()
            print()

        try:
            ans = int(ans)
        except ValueError:
            print()
            print("Not an integer.")
            print()
            sleep(1)
            
    
if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    