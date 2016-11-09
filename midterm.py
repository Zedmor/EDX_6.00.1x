#!/bin/python
def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''

    # closest_power(3, 12)
    # returns
    # 2
    # closest_power(4, 12)
    # returns
    # 2
    # closest_power(4, 1)
    # returns
    # 0

    #base ** x = ~num

    #Gradient descent
    #Начать с 0 и измерять расстояние. If
    def ln(x):
        n = 10000.0
        return n * ((x ** (1 / n)) - 1)

    def log(x,base):
        return(ln(x)/ln(base))

    x = base**(round(log(num,base)))
    y = base**(round(log(num,base)-1))
    if  (x-y)/2+x==num:return(y)
    else:
        return(x)

print(closest_power(9,70))


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    return(sum([a*b for a,b in zip(lista,listb)]))

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
    #global L
    L [:]= list(reversed([list(reversed(a)) for a in L]))

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
deep_reverse(L)
print(L)

def foo(X):
    M=X
    X=[1,2,3]

Z = [3,2,1]
print(Z)
foo(Z)
print(Z)


def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    int_d={}
    d1keys=list(d1.keys())
    d2keys=list(d2.keys())
    intr=list(set(d1keys).intersection(d2keys))
    for i in intr:
        int_d[i]=f(d1[i],d2[i])
    diff_d={}
    for i in set(d1)-set(intr):
        diff_d[i]=d1[i]
    for i in set(d2) - set(intr):
        diff_d[i] = d2[i]
    return(int_d,diff_d)


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    bln = [g(f(i)) for i in L]
    L[:] = filtered_list = [i for (i, v) in zip(L, bln) if v]
    if len(L)>0: return(max(L))
    else:
        return(-1)

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    #if not(any(isinstance(element, list) for element in aList)):return(aList)
    def Flat1List(zlist):
        """
        :param zlist: Input list with exactly ONE nested list
        :return: list with that list flattened
        """
        z=[]
        for i in zlist:
            if type(i)==list:
                for a in i:
                    z.append(a)
            else:
                z.append(i)
        return(z)

    x = aList
    if sum(isinstance(i, list) for i in aList)==0: return(x)
    else:
        return(flatten(Flat1List(x)))



    for i in aList:
        if
    NumLists=sum(isinstance(i, list) for i in aList)
    if NumLists==0: return(aList)
    while NumLists >0:

        NumLists-=1
    return(z)
    return([flatten(i) for i in aList])