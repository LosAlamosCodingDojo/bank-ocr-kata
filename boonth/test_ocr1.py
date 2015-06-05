"""
Tests for ocr1. Meant to be run with py.test.

usage: py.test -v test_ocr1.py

"""

import os
import sys

import ocr1_adaptor

def test_00():
    """Test of reading 0"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '| || || || || || || || || |\n'
             '|_||_||_||_||_||_||_||_||_|\n'
             '                           ')
    expected_output = ('000000000\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_01():
    """Test of reading 1"""

    input = ('                           \n'
             '  |  |  |  |  |  |  |  |  |\n'
             '  |  |  |  |  |  |  |  |  |\n'
             '                           ')
    expected_output = ('111111111\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_02():
    """Test of reading 2"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
             '                           ')
    expected_output = ('222222222\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_03():
    """Test of reading 3"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             ' _| _| _| _| _| _| _| _| _|\n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '                           ')
    expected_output = ('333333333\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_04():
    """Test of reading 4"""

    input = ('                           \n'
             '|_||_||_||_||_||_||_||_||_|\n'
             '  |  |  |  |  |  |  |  |  |\n'
             '                           ')
    expected_output = ('444444444\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_05():
    """Test of reading 5"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '                           ')
    expected_output = ('555555555\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_06():
    """Test of reading 6"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
             '|_||_||_||_||_||_||_||_||_|\n'
             '                           ')
    expected_output = ('666666666\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_07():
    """Test of reading 7"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '  |  |  |  |  |  |  |  |  |\n'
             '  |  |  |  |  |  |  |  |  |\n'
             '                           ')
    expected_output = ('777777777\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_08():
    """Test of reading 8"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '|_||_||_||_||_||_||_||_||_|\n'
             '|_||_||_||_||_||_||_||_||_|\n'
             '                           ')
    expected_output = ('888888888\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_09():
    """Test of reading 9"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '|_||_||_||_||_||_||_||_||_|\n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '                           ')
    expected_output = ('999999999\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_all():
    """Test of reading all digits in order"""

    input = ('    _  _     _  _  _  _  _ \n'
             '  | _| _||_||_ |_   ||_||_|\n'
             '  ||_  _|  | _||_|  ||_| _|\n'
             '                           ')
    expected_output = ('123456789\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

def test_multi():
    """Test of reading multiple account numbers"""

    input = ('                           \n'
             '  |  |  |  |  |  |  |  |  |\n'
             '  |  |  |  |  |  |  |  |  |\n'
             '                           \n'
             ' _  _  _  _  _  _  _  _  _ \n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
             '                           \n'
             ' _  _  _  _  _  _  _  _  _ \n'
             ' _| _| _| _| _| _| _| _| _|\n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '                           \n'
             '    _  _     _  _  _  _  _ \n'
             '  | _| _||_||_ |_   ||_||_|\n'
             '  ||_  _|  | _||_|  ||_| _|\n'
             '                           ')
                           
    expected_output = ('111111111\n'
                       '222222222\n'
                       '333333333\n'
                       '123456789\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr1_adaptor.run_ocr(input)
    assert output == expected_output

