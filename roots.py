# f1 = x^2 - 17x + 71
# f2 = x^2 - 34x + 240
#
# find all integer roots x which satisfy
# f1 ^ f2 == 1
# give back their sum

import numpy as np
import sys

def f1(x):
  return x * x - 17 * x + 71

def f2(x):
  return x * x - 34 * x + 240


if __name__ == '__main__':
    
    if sys.argv[1] == 'debug':
        debug = True
    else:
        debug = False
    
    ## coefficients of polynomials
    ## x^2 - 17x + 71 = 1
    p1_m1 = [1, -17, 70]
    ## x^2 - 17x + 71 = -1
    p1_p1 = [1, -17, 72]
    ## x^2 - 34x + 240 = 0
    p2 = [1, -34, 240]
    
    ## get the roots
    p1_m1_roots = np.roots(p1_m1)
    p1_p1_roots = np.roots(p1_p1)
    p2_roots = np.roots(p2)

    if debug:
        print 'f1 = 1 roots: %s' % p1_m1_roots
        print 'f1 = -1 roots: %s' % p1_p1_roots
        print 'f2 = 0 roots: %s' % p2_roots
    
    ## gather roots
    xs = np.hstack((p1_m1_roots, p1_p1_roots, p2_roots))
    
    ## transform to integers
    xs = np.unique(np.array([int(round(x)) for x in xs], dtype=int))
    
    if debug:
        print 'unique roots: %s' % xs
    
    ## roots that satisfy f1 ^ f2 == 1
    valid = []
    if debug:
        print 'x\tf1\tf2\tcalc\tsatisfied?'
        print '-\t--\t--\t----\t----------'
    
    for x in xs:
        temp = f1(x) ** f2(x)
        if debug:
            print '%d\t%d\t%d\t%d\t%r' % (x, f1(x), f2(x), temp, temp == 1)
        
        # if satisfied, collect it
        if temp == 1:
            valid.append(x)

    print 'these make the count: %s' % valid
    print 'sum: %d' % sum(valid)
