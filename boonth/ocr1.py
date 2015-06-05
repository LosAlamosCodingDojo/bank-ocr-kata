"""Parse a file containing bank account numbers. Print all of them out."""

import sys

import ocr

def main(input):
    """Take a file and parse LCD numbers into normal numbers. Prints out all
    account numbers.
    
    """

    fin = open(input, 'r')

    while True:
        account, lcd_account = ocr.getNextAccountNumber(fin)
        if account is None:
            break
        else:
            print account

    fin.close()


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'usage: <input>'
    else:
       main(sys.argv[1])
