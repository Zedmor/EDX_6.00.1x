def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def result(x):
        res = 0
        for i in range(len(L)):
            res+=L[i]*x**(len(L)-i-1)
        return res
    return result

print ( general_poly([1, 2, 3, 4])(10) )