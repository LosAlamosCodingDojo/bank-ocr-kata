"""
Parse a file containing bank account numbers. Prints out special
notifications of account numbers are illegible or have a bad checksum.

"""

import sys

import ocr

def main(input):
    """Take a file and parse LCD numbers into normal numbers"""

    fin = open(input, 'r')

    while True:
        account, lcd_account = ocr.getNextAccountNumber(fin)
        if account is None:
            # no more account numbers left in the file
            break

        if account.count('?') > 0:
            # illegible number
            print account, 'ILL'
        elif ocr.validChecksum(account):
            # good account number
            print account
        else:
            # invalid checksum
            print account, 'ERR'

    fin.close()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'usage: <input>'
    else:
       main(sys.argv[1])

