# Import things
import sys
import os

# Begin the KeyboardInterrupt loop
try:

    # Introduction
    os.system('clear')
    print('PRICE CALCULATOR')
    print('Enter the prices and weights or amounts of products that need to be compared. Enter as many values as necessary.')
    print('If you are done, enter 0 as the weight of the next product.')
    print('')

    # Set variables
    weightTwo = float(-1)
    counter = 1
    ppuOne = 0
    ppuTwo = 0
    weightOne = raw_input('Enter the amount or weight of a product: ')
    try:
        weightOne = float(weightOne)
        if weightOne <= 0:
            sys.exit('Product 1 apparently does not exist, check values and run program again.')
    except ValueError:
        sys.exit('Invalid value entered, try again')
    priceOne = raw_input('Enter the price of a product: ')
    try:
        priceOne = float(priceOne)
        if priceOne == 0:
            sys.exit('Product 1 is free')
        if priceOne < 0:
            sys.exit('Prices cannot be negative, check values and run program again.')
    except ValueError:
        sys.exit('Invalid value entered, try again')
    while weightTwo != float(0):
        weightTwo = raw_input('Enter the amount or weight of another product: ')
        try:
            weightTwo = float(weightTwo)
            if weightTwo == 0:
                print('')
                if ppuOne == ppuTwo:
                    print('The Price per unit (PPU) is the same.')
                    print 'PPU: ', ppuOne
                if ppuOne < ppuTwo:
                    print 'Product', counter,'is the cheapest.'
                    print('Here is its price per unit compared to the last product entered:')
                    print 'PPU: ',ppuOne,'VS',ppuTwo
                if ppuOne > ppuTwo:
                    print 'Product', counter,'is the cheapest.'
                    print('Here is its price per unit compared to the last product entered:')
                    print 'PPU: ',ppuTwo,'VS',ppuOne
                print('')
                sys.exit()
            if weightTwo <= 0:
                sys.exit('The product apparently does not exist, check values and run program again.')
        except ValueError:
            sys.exit('Invalid value entered, try again')
        priceTwo = raw_input('Enter the price of another product: ')
        try:
            priceTwo = float(priceTwo)
            if priceTwo < 0:
                sys.exit('Prices cannot be negative, check values and run program again.')
            if priceTwo == 0:
                sys.exit('The product is is free')
        except ValueError:
            sys.exit('Invalid value entered, try again')
        
        # Calculations    
        ppuOne = priceOne / weightOne
        ppuTwo = priceTwo / weightTwo
        
        # Evaluations
        if (ppuOne) == (ppuTwo):
            priceOne = float((priceOne))
            weightOne = float((weightOne))
        if (ppuOne) < (ppuTwo):
            priceOne = float((priceOne))
            weightOne = float((weightOne))
        if (ppuOne) > (ppuTwo):
            priceOne = float((priceTwo))
            weightOne = float((weightTwo))
            counter = (counter) + 1
    print('')

# End the KeyboardInterrupt loop
except KeyboardInterrupt:
    print('')
    sys.exit()