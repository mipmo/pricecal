# pricecal
This is the Python implementation of the price comparison program I wrote on the TI-84 Plus CE-T.

#### What it does and how it works
The Price Calculator can compare the prices of products, regardless of their weight or amount.
It does this by comparing the Price Per Unit (PPU) of the  products, which it can calculate from the entered price and amount.
This program can compare any amount of products. To do this, it "cheats" somewhat: Rather than storing all inputs, it overwrites the first variable with the currently cheapest product, comparing it to the next one the user enters. It only outputs the final result once the user enters '0' as the weight of a product. As such, it is not capable of displaying a list of every product entered, since old values are overwritten.
The instructions on how to use this program are in the program itself; to run it, simply enter './pricecal' at the terminal.  
