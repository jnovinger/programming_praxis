#!/usr/bin/python

from math import sqrt
import sys

def sieve(limit):
    sieve = range(3, limit, 2)
        
    for divisor in sieve:
        if divisor > sqrt(limit):
            #print "Divisor bigger than sqrt of limit, breaking\n"
            break
        for number in sieve:
            if not number % divisor and number != divisor:
                #print "number:", number, "divisor:", divisor, " ... removing"
                sieve.remove(number)
    
    sieve.insert(0, 2)
    return sieve

if __name__ == '__main__':
  
    limit = 1000
    print sieve(limit)
