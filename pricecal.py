# Import things
import sys
import os

# Begin the KeyboardInterrupt loop
try:

# Introduction
    os.system('clear')
    print('PRICE CALCULATOR')
    print('For use with two products')
    print('If more prices need to be compared, run the program again using the cheaper product as the starting product.')
    print('')

# Set variables
    a = raw_input('Enter the amount or weight of the first product: ')
    try:
        a = float(a)
    except ValueError:
        sys.exit('Invalid value entered, try again')
    b = raw_input('Enter the price of the first product: ')
    try:
        b = float(b)
    except ValueError:
        sys.exit('Invalid value entered, try again')
    c = raw_input('Enter the amount or weight of the second product: ')
    try:
        c = float(c)
    except ValueError:
        sys.exit('Invalid value entered, try again')
    d = raw_input('Enter the price of the second product: ')
    try:
        d = float(d)
    except ValueError:
        sys.exit('Invalid value entered, try again')
    print('')

# Checks for invalid numbers
    if a <= 0:
        sys.exit('Product 1 does not exist, check values and run program again.')
    if c <= 0:
        sys.exit('Product 2 does not exist, check values and run program again.')
    if b == 0:
        sys.exit('Product 1 is free')
    if d == 0:
        sys.exit('Product 2 is free')
    if b < 0:
        sys.exit('Prices cannot be negative, check values and run program again.')
    if d < 0:
        sys.exit('Prices cannot be negative, check values and run program again.')

# Calculations
    e = b / a
    f = d / c

# Evaluation and output
    if e == f:
        print('The Price per unit (PPU) is the same.')
        print 'PPU: ', e
    if e < f:
        print('Product 1 is cheaper.')
        print 'PPU: ',e,'VS',f
    if e > f:
        print('Product 2 is cheaper.')
        print 'PPU: ',e,'VS',f
    print('')

# Outroduction
    print('To compare more products, run this program again.')

# End the KeyboardInterrupt loop
except KeyboardInterrupt:
    print('')
    sys.exit()