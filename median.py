#!/usr/bin/python2.7
from __future__ import division
import itertools

def merged(a, b):
    """Generator to step through all items of two sorted iterators in order."""
    i = 0
    j = 0
    while i<len(a) and j<len(a):
        while i < len(a) and a[i] <= b[j]:
            yield a[i]
            i += 1
        while j < len(b) and b[j] <= a[i]:
            yield b[j]
            j += 1
    while i < len(a):
        yield a[i]
        i += 1
    while j < len(b):
        yield b[j]
        j += 1


def median(a, b):
    N = len(a) + len(b)
    if N % 2 == 1:
        return itertools.islice(merged(a, b), N//2, None).next()
    else:
        nums = itertools.islice(merged(a, b), N/2 - 1, N/2 + 1)
        return (nums.next() + nums.next()) / 2

if __name__ == '__main__':
    a = [2, 4, 18, 33, 34, 56, 76]
    b = [7, 8, 26, 39, 44, 45, 90]
    print 'a:', a
    print 'b:', b
    print 'median:', median(a, b)

