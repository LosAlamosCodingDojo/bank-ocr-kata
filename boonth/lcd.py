"""
Contains the base operations for dealing with LCD digits. The basic data
structure is a 3x3 array of chars, called an LCD digit.

"""

import numpy

def blankLCDDigit():
    """Return a blank LCD Digit"""

    return numpy.full((3,3), ' ', dtype='S1')

def printLCDDigit(d):
    """Print out an lcd digit. Add quotes around it to see whitespace."""

    for i in range(3):
        print "\'" + d[i][0] + d[i][1] + d[i][2] + "\'"
    print ''

