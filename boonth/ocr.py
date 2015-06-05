"""
Base operations for the Bank OCR kata. The basic data structure is a 3x3
array of chars, called an LCD Digit.

"""

import numpy

import lcd
import numbers


def newAccountNumber():
    """Return an array of 9 blank LCD digits"""

    account = []
    for i in range(9):
        account.append(lcd.blankLCDDigit())
    return account

def LCDtoStr(lcd_digit):
    """Given an LCD digit, return corresponding string representation"""

    # in order to hash the numpy array, we need to make it read-only, so 
    # make it read-only, then set it back to normal later
    lcd_digit.flags.writeable = False
    result = None
    if lcd_digit.data in numbers.LCDtoStr:
        result = numbers.LCDtoStr[lcd_digit.data]
    else:
        # unknown LCD, return ?
        result = '?'

    lcd_digit.flags.writeable = True
    return result

def StrtoLCD(digit_str):
    """Given a digit as a string, return corresponding lcd digit"""

    if digit_str in numbers.StrtoLCD:
        return numbers.StrtoLCD[digit_str]
    else:
        return None

def getNextAccountNumber(f):
    """Parse a file containing bank account numbers. Return the next account
    number as a string and the account as LCD digits. If there are no
    more account numbers, return None, None.
    
    """

    # read in number as 3x3 array of characters
    line = f.readline()

    if line == '':
        return None, None

    # create new blank account number
    account = newAccountNumber()

    # read in an account number as LCD digits
    for i in range(3):          # for each line in file
        for d in range(9):      # for each digit
            for j in range(3):  # for each column
                account[d][i][j] = line[d*3 + j]
        line = f.readline()

    # find out which number the digits actually are
    account_str = ''
    for digit in account:
        digit_str = LCDtoStr(digit)
        account_str += digit_str

    return account_str, account

def validChecksum(account):
    """Given an account number (string), return whether the account number has
    a valid checksum or not.
    
    """

    digits = list(str(account))
    digits = [int(d) for d in digits]
    sum = 0
    for i, n in enumerate(digits):
        sum += n * (9 - i)

    if sum % 11 == 0:
        return True
    else:
        return False

def getEditDistance(lcd1, lcd2):
    """Given two lcd digits, return the edit distance between them. The edit
    distance is the number of operations required to change one digit to the
    other. Essentially count the number of differing characters between the
    two.
    
    """

    # do some numpy operations. the equality check will do element-wise
    # comparisons, and the output is an array of True and False's. we want to
    # count the number of False's, so first 'not' the array, and count the
    # number of True's 
    compare = lcd1 == lcd2
    return numpy.count_nonzero(numpy.logical_not(compare))
