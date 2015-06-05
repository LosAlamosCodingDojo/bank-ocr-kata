"""
Hard code what each digit looks like in the LCD digit data structure.  Also
create a dict that maps an LCD digit to its string representation. In order to
make a numpy array hashable, it needs to be read-only.

"""

import lcd

zero = lcd.blankLCDDigit()
zero[0] = list(' _ ')
zero[1] = list('| |')
zero[2] = list('|_|')
zero.flags.writeable = False

one = lcd.blankLCDDigit()
one[0] =  list('   ')
one[1] =  list('  |')
one[2] =  list('  |')
one.flags.writeable = False

two = lcd.blankLCDDigit()
two[0] =  list(' _ ')
two[1] =  list(' _|')
two[2] =  list('|_ ')
two.flags.writeable = False

three = lcd.blankLCDDigit()
three[0] = list(' _ ')
three[1] = list(' _|')
three[2] = list(' _|')
three.flags.writeable = False

four = lcd.blankLCDDigit()
four[0] = list('   ')
four[1] = list('|_|')
four[2] = list('  |')
four.flags.writeable = False

five = lcd.blankLCDDigit()
five[0] = list(' _ ')
five[1] = list('|_ ')
five[2] = list(' _|')
five.flags.writeable = False

six = lcd.blankLCDDigit()
six[0] = list(' _ ')
six[1] = list('|_ ')
six[2] = list('|_|')
six.flags.writeable = False

seven = lcd.blankLCDDigit()
seven[0] = list(' _ ')
seven[1] = list('  |')
seven[2] = list('  |')
seven.flags.writeable = False

eight = lcd.blankLCDDigit()
eight[0] = list(' _ ')
eight[1] = list('|_|')
eight[2] = list('|_|')
eight.flags.writeable = False

nine = lcd.blankLCDDigit()
nine[0] = list(' _ ')
nine[1] = list('|_|')
nine[2] = list(' _|')
nine.flags.writeable = False

all_digits = [zero, one, two, three, four, five, six, seven, eight, nine]

LCDtoStr = {zero.data  : '0',
            one.data   : '1',
            two.data   : '2',
            three.data : '3',
            four.data  : '4',
            five.data  : '5',
            six.data   : '6',
            seven.data : '7',
            eight.data : '8',
            nine.data  : '9'}

StrtoLCD = {'0' : zero,
            '1' : one,
            '2' : two,
            '3' : three,
            '4' : four,
            '5' : five,
            '6' : six,
            '7' : seven,
            '8' : eight,
            '9' : nine}
