"""
Tests for ocr4. Meant to be run with py.test.

usage: py.test -v test_ocr4.py

"""

import os
import sys

import ocr4_adaptor

def test_00():
    """Test"""

    input = ('                           \n'
             '  |  |  |  |  |  |  |  |  |\n'
             '  |  |  |  |  |  |  |  |  |\n'
             '                           ')
    expected_output = ('711111111\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_01():
    """Test"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '  |  |  |  |  |  |  |  |  |\n'
             '  |  |  |  |  |  |  |  |  |\n'
             '                           ')
    expected_output = ('777777177\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_02():
    """Test"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             ' _|| || || || || || || || |\n'
             '|_ |_||_||_||_||_||_||_||_|\n'
             '                           ')
    expected_output = ('200800000\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_03():
    """Test"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             ' _| _| _| _| _| _| _| _| _|\n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '                           ')
    expected_output = ('333393333\n')
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_04():
    """Test"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '|_||_||_||_||_||_||_||_||_|\n'
             '|_||_||_||_||_||_||_||_||_|\n'
             '                           ')
    expected_output=("888888888 AMB ['888886888', '888888880', '888888988']\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_05():
    """Test"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '                           ')
    expected_output=("555555555 AMB ['555655555', '559555555']\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_06():
    """Test"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
             '|_||_||_||_||_||_||_||_||_|\n'
             '                           ')
    expected_output=("666666666 AMB ['666566666', '686666666']\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_07():
    """Test"""

    input = (' _  _  _  _  _  _  _  _  _ \n'
             '|_||_||_||_||_||_||_||_||_|\n'
             ' _| _| _| _| _| _| _| _| _|\n'
             '                           ')
    expected_output=("999999999 AMB ['899999999', '993999999', '999959999']\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_08():
    """Test"""

    input = ('    _  _  _  _  _  _     _ \n'
             '|_||_|| || ||_   |  |  ||_ \n'
             '  | _||_||_||_|  |  |  | _|\n'
             '                           ')
    expected_output=("490067715 AMB ['490067115', '490067719', '490867715']\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_09():
    """Test"""

    input = ('    _  _     _  _  _  _  _ \n'
             ' _| _| _||_||_ |_   ||_||_|\n'
             '  ||_  _|  | _||_|  ||_| _|\n'
             '                           ')
    expected_output=("123456789\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_10():
    """Test"""

    input = (' _     _  _  _  _  _  _    \n'
             '| || || || || || || ||_   |\n'
             '|_||_||_||_||_||_||_| _|  |\n'
             '                           ')
    expected_output=("000000051\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_11():
    """Test"""

    input = ('    _  _  _  _  _  _     _ \n'
             '|_||_|| ||_||_   |  |  | _ \n'
             '  | _||_||_||_|  |  |  | _|\n'
             '                           ')
    expected_output=("490867715\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

def test_12():
    """Test"""

    input = (' _  _  _  _  _  _  _  _    \n'
             '| || || || || || || ||_   |\n'
             '|_||_||_||_||_||_||_| _|  |\n'
             '                           ')
    expected_output=("000000051\n")
    expected_output = expected_output.replace('\n', os.linesep)

    output = ocr4_adaptor.run_ocr(input)
    assert output == expected_output

