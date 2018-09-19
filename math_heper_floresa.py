from math import *

'''
5 tests of the 5 formulas here
'''

def equation(x1,y1,x2,y2):
    '''Returns the equation of the line going through points (x1,y1)
       and (x2,y2) in slope intercept form; y = mx + b
       
    >>>equation(3,-2,5,-1)
    y = 1.5x - 3.5
    
    >>>equation(10,8,-5,5)
    y = 0.2x + 6.0
    
    >>>equation(-10,-15,-15,-20)
    y = 1.0x - 5.0

    >>>equation(5.8,9.2,5,4)
    y = 6.5x + -28.5
    '''
    
    slope = (y2 - y1) / (x2 - x1)
    mx = slope * x1
    intercept = y1 - mx
    print(f"The equation of the line going through points ({x1},{y1}) and ({x2,y2}) is y = {round(slope,2)}x + {round(intercept,2)}")

def heron(a,b,c):
    '''Returns the area of a triangle given sides a, b, and c
       The three sides must comply with the Triangle Inequality Theorem - The sum of the lengths
       of any two sides of a triangle is greater than the length of the third side.
       
       >>>heron(7,10,9)
       30.59
       
       >>>heron(100,135,226)
       3595.41
       
       >>>heron(4.4,5.5,7.708000)
       11.85
       
       >>>heron(75.3,26.75,110.07)
       Traceback (most recent call last:
        ...
        ValueError: Cannot square root a negative number
       
       >>>heron(75.3,26.75,9.07)
       Traceback (most recent call last):
        ...
        ValueError: Impossible input due to one side being to small

    '''
    s = (a + b + c) / 2
    ans = sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of a triangle from side {a}, {b}, and {c} is {round(ans, 2)}")

def quad(a,b,c):
    '''Returns two answers(zeros) using the quadratic formula for a quadratic equation
       Inputing the 'a' value, 'b' value, and 'c' value from
       ax^2 + bx + c = 0

    '''
    if ((b**2) - (4 * (a * c))) < 0:
        raise ValueError("Cannot square root a negative integer")
    
    ans1 = -(b) + sqrt((b**2) - (4*(a*c)))
    ans2 = -(b) - sqrt((b**2) - (4*(a*c)))
    
    
    final1 = ans1 / (2 * a)
    final2 = ans2 / (2 * a)
    
    print(f"The zeros of the quadratic equation {a}x^2 + {b}x + {c} = 0 is \n {round(final1,2)} and {round(final2,2)}")
    
    
def main():
    quad(3,4,5)
#    print('Enter coordinates of 2 points')
#    x1 = float(input('x1: '))
#    y1 = float(input('y1: '))
#    x2 = float(input('x2: '))
#    y2 = float(input('y2: '))
#    equation(x1,y1,x2,y2)
#    while True:
#        
#        print('Enter the sides of the triangle')
#        a = float(input('a: '))
#        b = float(input('b: '))
#        c = float(input('c: '))
#        if a + b <= c or b + c <= a:
#            pass
#        if a + c > b:
#            pass
#        else:
#            again += 1
#            print('Impossible input because of the Triangle Inequality Theorem')
#       
#     heron(a,b,c)
    
    

if __name__ == "__main__":
    main()
    