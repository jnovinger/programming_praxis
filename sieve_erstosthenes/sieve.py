#!/usr/bin/python

from math import sqrt
import sys

if __name__ == '__main__':

    
    limit = 1000000
    sieve = []
    
    for number in xrange(2,limit):
        sieve.append(number)
        
    for divisor in sieve:
        if divisor > sqrt(limit):
            print "Divisor bigger than sqrt of limit, breaking\n"
            break
        for number in sieve:
            if not number % divisor and number != divisor:
                print "number:", number, "divisor:", divisor, "removing:", number
                sieve.remove(number)
                
    print sieve
