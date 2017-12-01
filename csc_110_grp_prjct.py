from math import sqrt

def is_factor(n,f):
    '''
Returns True if f is a factor of n.
OTW returns False.  n is an int.
'''


def is_prime(n):
    '''
Returns True if n is prime,
OTW returns False.  n is a positive int.
'''
    if n == 1:
        return 1 == 0  # 1 is not prime for some reason.
    factors = 0
    for x in range(2, int(sqrt(n) + 1)):
        if n % x == 0:  # If you can divide by a number with no remainder it is a factor.
            factors += 1
        else:
            continue
    return factors == 0  # Returns True when there are zero factors aka number is prime.


def mult_of_factor(n,f):
    '''
Returns the multiplicity of f, that is
highest exponent of f that divides n.
e.g. multOfFactor(40,2) returns 3, since
2^3 is the highest power of 3 that divides 40.
If f does not divide n, it has a multiplicity of zero.
'''


def add_fractions(n1,d1,n2,d2):
    '''Returns the result of adding 2 fractions, each of which is
a tuple has ints ni and di  representing the numerator & denominator of
the fraction.  The fraction is returned reduced to lowest terms.'''


def next_prime(n):
    '''Returns the next prime bigger than n, assuming n is prime.
'''


def prime_factors_of(n):
    '''
Returns a dictionary of prime factors of n of the form
(p1:m1,p2:m2,...}, where pi is a prime & mi is the multiplicity of pi.
'''


def reduce(n,d):
    '''Returns the fraction, n/d , in lowest terms.'''

  
def gcd(n,m):
    '''Returns the greatest common divisor of int n and int m.'''


def lcm(n,m):
    '''Returns the least common mutiple of int n and int m.'''


def print_fraction(n,d):
    '''Prints the fraction represented by n/d.'''


def sum_series(n):
##    '''Uses the functions above to print the exact sum expressed as
##a fraction of n terms of the sum 1/1 + 1/2 + 1/3 + ... + 1/n, where n >= 1.'''

    

## sample run
print('multiplicity')
for (n,f) in [(24,2),(24,7),(24,3)]:
    print(n,f,multOfFactor(n,f))
print()





## sample run
print('nextPrime')
for n in [3,11,31]:
    print(n,nextPrime(n))
print()

        
                
## sample run
print('primeFactorsOf')
for n in range(2,13):
    print(n,primeFactorsOf(n))
print()



    

## sample run
print('gcd')
for (n,m) in ((12,20),(4,9),(112,24),(1234,4321),(7654,346),(1,7)):
    print(n,m,gcd(n,m))
print()
            


    

## sample run
print('lcm')            
for (n,m) in ((12,20),(4,9),(1,7)):
    print(n,m,lcm(n,m))           
print()

  
    

## sample run
print('reduce')
for (n,d) in [(1,2),(6,15)]:
    print(n,d,'prints as',reduce(n,d) )
print()



    

## sample run
print('add_fractions')
for (n1,d1,n2,d2) in [(1,2,1,4),(2,5,3,20)]:
    print(n1,d1,n2,d2,'adds to', add_fractions(n1,d1,n2,d2))
print()


## sample run
print('print_fraction')
for (n,d) in [(1,2),(3,4)]:
    print(n,d,'prints as', end = ' ')
    print_fraction(n,d) 
print()



## sample run
print('sum_series')
for n in range(3,7):
    print(n, end = ', ')
    sum_series(n)
print()


## SAMPLE RUNS
##multiplicity
##24 2 3
##24 7 0
##24 3 1
##
##nextPrime
##3 5
##11 13
##31 37
##
##primeFactorsOf
##2 {2: 1}
##3 {3: 1}
##4 {2: 2}
##5 {5: 1}
##6 {2: 1, 3: 1}
##7 {7: 1}
##8 {2: 3}
##9 {3: 2}
##10 {2: 1, 5: 1}
##11 {11: 1}
##12 {2: 2, 3: 1}
##
##gcd
##12 20 4
##4 9 1
##112 24 8
##1234 4321 1
##7654 346 2
##1 7 1
##
##lcm
##12 20 60
##4 9 36
##1 7 7
##
##reduce
##1 2 prints as (1, 2)
##6 15 prints as (2, 5)
##
##add_fractions
##1 2 1 4 adds to (3, 4)
##2 5 3 20 adds to (11, 20)
##
##print_fraction
##1 2 prints as 1/2
##3 4 prints as 3/4
##
##sum_series
##3, 11/6
##4, 25/12
##5, 137/60
##6, 49/20
