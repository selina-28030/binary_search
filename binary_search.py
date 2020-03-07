#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    length = len(xs)
    mid = length//2
    if length == 0:
        return None
    elif xs[mid] == 0:
        return mid + 1
    elif xs[mid] < 0:
        if length == 1:
            return None
        else:
            funct = find_smallest(xs[mid + 1:])
            if funct == None:
                return None
            else:
                return funct+mid+1
    else:
        if length ==1:
            return 0
        else:
            if find_smallest_positive(xs[:mid])== None:
                return mid
            else:
                return find_smallest_positive(xs[:mid])


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([1, 2, 3], 4)
    0
    '''
    first = first_occ(xs, x)
    last = last_occ(xs, x)
    if last == None or first == None:
        return 0
    else:
        if first!=last:
            return last-first
        else:
            return last-first+1
    def first_occ(xs, x):
        length = len(xs)
        middle = length//2
        if length == 0:
            return None
        elif length ==1 and xs[0] ==x:
            return 0
        elif xs[middle] == x:
            if xs[middle-1] != x:
                return middle
            else:
                return first_occ(xs[:middle], x)
        elif xs[middle] > x:
            funct = first_occ(xs[middle+1:], x)
            if funct == None:
                return None
            else:
                return func+middle+1
        else:
            return first_occ(xs[:middle], x)

    def last_occ(xs, x):
        length = len(xs)
        middle = length//2
        if length == 0:
            return 0
        elif length ==1 and xs[0] == x:
            return 1
        elif xs[middle] == x:
            if middle == length -1:
                return middle
            elif xs[middle+1] != x:
                return middle
            else:
                funct = last_occ(xs[middle+1:], x)
                if funct == None:
                    return None
                else:
                    return funct+middle+1
        elif xs[middle] > x:
            funct = last_occ(xs[middle+1:], x)
            if funct == None:
                return None
            else:
                return funct+middle+1
        else:
            return last_occ(xs[:middle], x)


def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    m1 = (hi- lo)/3 + lo
    m2 = hi - ((hi-lo)/3)
    flo = f(lo)
    fm1 = f(m1)
    fm2 = f(m2)
    fhi = f(hi)
    minimum = min(flo, fm1, fm2, fhi)
    if hi-lo < epsilon:
        if fhi == min(flo, fhi):
            return hi
        if flo == min(flo, fhi):
            return lo
    if flo == minimum or fm1 == minimum:
        return argmin(f,lo, m2, epsilon = epsilon)
    else:
        return argmin(f,m1, hi, epsilon = epsilon)
