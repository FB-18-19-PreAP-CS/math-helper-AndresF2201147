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
    s = (a + b + c) / 2
    ans = sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of  atriangle from side {a}, {b}, and {c} is {round(ans, 2)}")


def main():
    equation(5.8,9.2,5,4)
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
#        if a + b > c:
#            pass
#        if b + c > a:
#            pass
#        if a + c > b:
#            pass
#        else:
#            again += 1
#            print('Impossible input because of the Triangle Inequality Theorem')
        
    #heron(a,b,c)
    
    

if __name__ == "__main__":
    main()
    