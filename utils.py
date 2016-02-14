# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
from math import sqrt

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    i=1

    if type(n) is str:
        raise TypeError
    if n<0:
        raise ValueError

    if n==0:
        return 1
    while n>0:
        i*=n
        n-=1
    if n==0:
        return i


def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    if a ==0:
            if b==0:
                tuple=()
                return tuple
            sol1=(-c)/(b)
            tuple=(sol1,)

            return tuple

    delta=(b**2)-(4*a*c)
    if delta >0:
        sol1=((-b+sqrt(delta))/(2*a))
        sol2=((-b-sqrt(delta))/(2*a))
        tuple=(sol1,sol2)
        return tuple
    elif delta==0:
        sol1=((-b)/(2*a))
        tuple=(sol1)
        return tuple
    else:
        tuple=()
        return tuple

def integrate(a, b, c):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    try:
        p=1/4 #precision
        q=c-b
        r=b
        fonction=a
        res=0
        while c>r:
            x=r+p*(0.5)
            f=eval(fonction)
            res+=(f*p)
            r+=p
        return res
    except SyntaxError:
        return 'fonction non valide'


if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))