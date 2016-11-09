def primeFactors(n):
    import math
    def gen_primes():
        D = {}
        q = 2
        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            q += 1
    factors = {}
    gen = gen_primes()
    i = next(gen)
    while i<=int(math.sqrt(n)):
        if n//i==n/i:
            n=n//i
            if i in factors.keys():
                factors[i] += 1
            else: factors[i] =1
            # print('(', i, '**', factors[i], ')', end='', sep='')
        else:
            i=next(gen)
    factors[n] = 1
    strin = ''
    for i in sorted(factors.keys()):
        if factors[i]>1:
            strin+='('+ str(i)+ '**' + str(factors[i])+ ')'
        else:
            strin+='('+str(i)+')'
    return(strin)



print(primeFactors(7775460))