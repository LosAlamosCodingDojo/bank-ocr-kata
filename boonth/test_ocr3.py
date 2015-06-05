"""
Tests for ocr3. Meant to be run with py.test.

usage: py.test -v test_ocr3.py

"""

import os
import sys

import ocr3_adaptor

def test_00():
    """Account number with valid checksum"""

    input = (' _  _  _  _  _  _  _  _    \n'
             '| || || || || || || ||_   |\n'
             '|_||_||_||_||_||_||_| _|  |\n'
             '                           ')
    expected_output = ('000000051\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr3_adaptor.run_ocr(input)
    assert output == expected_output

def test_01():
    """Account number with illegible number"""

    input = ('    _  _  _  _  _  _     _ \n'
             '|_||_|| || ||_   |  |  | _ \n'
             '  | _||_||_||_|  |  |  | _|\n'
             '                           ')
    expected_output = ('49006771? ILL\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr3_adaptor.run_ocr(input)
    assert output == expected_output

def test_02():
    """Account number with multiple illegible numbers"""

    input = ('    _  _     _  _  _  _  _ \n'
             '  | _| _||_| _ |_   ||_||_|\n'
             '  ||_  _|  | _||_|  ||_| _ \n'
             '                           ')
    expected_output = ('1234?678? ILL\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr3_adaptor.run_ocr(input)
    assert output == expected_output

def test_03():
    """Account number with bad checksum"""

    input = (' _  _     _  _        _  _ \n'
             '|_ |_ |_| _|  |  ||_||_||_ \n'
             '|_||_|  | _|  |  |  | _| _|\n'
             '                           ')
    expected_output = ('664371495 ERR\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr3_adaptor.run_ocr(input)
    assert output == expected_output

