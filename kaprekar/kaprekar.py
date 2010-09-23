#!/usr/bin/python

def is_kaprekar(num):
    # k = num
    # n = digits
 
    num_digits = len(str(num))  # number of digits in num
 
    sqr = num * num             # k squared
    sqr_digits = len(str(sqr))  # number of digits in sqr
    
    left = int(str(sqr)[0:num_digits])
    left_1 = int(str(sqr)[0:num_digits - 1])
    right = int(str(sqr)[num_digits - 1:sqr_digits])
    
    
    print "num: ", num
    print "num_digits: ", num_digits
    print "sqr: ", sqr
    print "sqr_digits: ", sqr_digits
    print "left: ", left
    print "left_1: ", left_1
    print "right: ", right
    print "right + left: ", right + left
    print "right + left_1: ", right + left_1, "\n"
    
    if (right + left) == num:
        return True
    if (right + left_1) == num:
        return True

    return False
    
nums = []

for num in range (10,1000):
    if is_kaprekar(num) == True:
        nums.append(num)

print nums
