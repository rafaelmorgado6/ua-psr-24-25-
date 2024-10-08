
from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x, y):
    real = x.r + y.r
    im = x.i + y.i
    result = Complex(real, im)
    
    return result

def multiplyComplex(x, y):
    result = Complex(x.r*y.r -  x.i*y.i, x.r*y.i + x.i*y.i)
    
    return result

def printComplex(x):
    
    print(f"{x.r} + {x.i}i")

def main():
    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1)) # named tuple looks nice when printed

    c3 = addComplex(c1, c2)
    printComplex(c3)

    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()