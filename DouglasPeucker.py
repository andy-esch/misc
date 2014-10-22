#/bin/sh python

import sys
from numpy import sqrt

points = [[  0.        ,   1.39462614],
       [  1.        ,   5.49726544],
       [  2.        ,   4.67564375],
       [  3.        ,   7.90361728],
       [  4.        ,   7.00751443],
       [  5.        ,   6.73286588],
       [  6.        ,   8.03163413],
       [  7.        ,  10.4834738 ],
       [  8.        ,  10.27900257],
       [  9.        ,  12.62013155]]

if len(sys.argv) > 1:
    epsilon = float(sys.argv[1])
    print "epsilon = %f" % epsilon
else:
    epsilon = 20.

def xstar(p,m,b):
    num = m * (p[1] - b) + p[0]
    denom = 1. + m * m
    return num / denom

def ystar(p,m,b):
    num = m * (m * p[1] + p[0]) + b
    denom = 1. + m * m
    return num / denom

def line(p1,p2):
    """
        Given two points of the form (x,y), return the slope and y-intercept
    """
    m = (p1[1] - p2[1]) / (p1[0] - p2[0])
    b = m * p1[0] - p1[1]
    return m, b

def shortestDistanceToSegment(p,m,b):
    """
        Equation from minimizing the distance from a point to a line
    """
    return abs(p[1] - m * p[0] - b) / sqrt(1. + m * m)

def DP(plist,ep):
    index = 0
    d = 0
    dmax = 0
    end = len(plist)
    for i in range(1,end):
        m, b = line(plist[0],plist[-1])
        d = shortestDistanceToSegment(plist[i],m,b)
        
        if (d > dmax):
            index = i
            dmax = d
            print "d = %f, i = %d" % (d,i)
    
    if (dmax > ep):
        r1 = DP(plist[0:index],ep)
        r2 = DP(plist[index:],ep)
        result = r1 + r2
    else:
        result = plist
    
    return result

if __name__ == '__main__':
    res = DP(points,epsilon)
    if (len(points) == len(res)):
        print "DP didn't clip array"
    print res
