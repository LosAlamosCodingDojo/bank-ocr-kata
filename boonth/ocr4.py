"""
Parse a file containing bank account numbers. If an account number is
illegible or has a bad checksum, try to find a more correct account number by
adding or removing one character.

"""

import copy
import sys

import lcd
import numbers
import numpy
import ocr

def main(input):
    """Take a file and parse LCD numbers into normal numbers"""

    fin = open(input, 'r')

    while True:
        account, lcd_account = ocr.getNextAccountNumber(fin)
        if account is None:
            # no more account numbers left in the file
            break

        if account.count('?') == 0 and ocr.validChecksum(account):
            # account number is OK
            print account
        elif account.count('?') == 1:
            # illegible number, try to find alternative possibilities
            alternatives = getIllPossibilities(account, lcd_account)
            if len(alternatives) == 0:
                # no possible alternatives
                print account, 'ILL'
            elif len(alternatives) == 1:
                print alternatives[0]
            else:
                print account, 'AMB', alternatives
        elif not ocr.validChecksum(account):
            # invalid checksum, try to find alternative possibilities
            alternatives = getErrPossibilities(account, lcd_account)
            if len(alternatives) == 0:
                # no possible alternatives
                print account, 'ERR'
            elif len(alternatives) == 1:
                print alternatives[0]
            else:
                print account, 'AMB', alternatives
        else:
            # invalid account number in some way, such as having 
            # multiple illegible characters
            if account.count('?') > 0:
                print account, 'ILL'
            else:
                print account, 'ERR'

    fin.close()

def getIllPossibilities(account_str, lcd_account):
    """Given 9 LCD digits, where one digit is illegible, return all possible
    account numbers with valid checksums that can be reached by adding or
    removing one character. Returns a list of strings, sorted ascending.
    
    """

    # all possible alternatives for the account number (output)
    alternatives = []

    # find the index of the illegible number, and extract
    # the illegible LCD digit
    d = account_str.find('?')
    ill_digit = lcd_account[d]

    # for each lcd number, calculate the edit distance from it to the illegible
    # lcd digit, keep the ones where the edit distance is 1, and checkums is
    # valid
    for lcd_digit in numbers.all_digits:
        distance = ocr.getEditDistance(ill_digit, lcd_digit)
        if distance == 1:
            alt = account_str.replace('?', ocr.LCDtoStr(lcd_digit))
            if ocr.validChecksum(alt):
                alternatives.append(alt)

    alternatives.sort()
    return alternatives

def getErrPossibilities(account_str, lcd_account):
    """Given 9 LCD digits, where all digits are legible, but the checksum is
    invalid, return all possible account numbers with valid checksums that can
    be reached by adding or removing one character.  Returns a list of
    strings, sorted ascending.
    
    """

    # all possible alternatives for the account number (output)
    alternatives = []

    for i in range(len(account_str)):
        # find all possibilities from changing the i-th digit
        acc_digit = ocr.StrtoLCD(account_str[i])
        for lcd_digit in numbers.all_digits:
            distance = ocr.getEditDistance(acc_digit, lcd_digit)
            if distance == 1:
                digit = ocr.LCDtoStr(lcd_digit)
                alt = account_str[:i] + digit + account_str[i+1:]
                if ocr.validChecksum(alt):
                    alternatives.append(alt)

    alternatives.sort()
    return alternatives


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'usage: <input>'
    else:
       main(sys.argv[1])


