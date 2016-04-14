# april 13, 2016
# which is larger?
# f1         f2
# 2^(30!) or (2^30)!

# f1
# --> log(2^(30!)) = 30! 
#
# Using Stirling's Approximation: n! ~ sqrt(2pi * n) * (n / e) ^ n  
# let n = 30, then 
# n! ~ sqrt(2pi * 2 * 15) * (30 / e) ^ 30
#    ~ 2 * sqrt(5pi) * 2 ^ 30 * 5 ^ 30
#    > sqrt(5pi) * 2^31 * 4^30
#    ~ sqrt(5pi) * 2^91
#    ~ 2^91
# therefore, f1 > 2^91


# f2
# --> log((2^30)!) = 2^30 * (2^30 + 1) / 2 = 2^29 * (2^30 + 1) ~ 2^59
# i.e., let 2^30 = x
## then log(x!) = x + (x-1) + (x-2) + ...
##              = x + x + x ... + x - (1 + 2 + 3 + ... + x - 1)
##              = x^2 - x * (x-1) / 2
##              = x * (x + 1) / 2

## therefore, since 2^91 < f1 and f2 < 2^87, f2 < f1


from scipy.special import factorial
from math import log

def two_to_n(n):
    return 1 << int(n)

if __name__ == '__main__':
    for n in range(10):
        print '%5.0f\t%5.0f' % (factorial(n), float(n * (n-1)) / 2.)