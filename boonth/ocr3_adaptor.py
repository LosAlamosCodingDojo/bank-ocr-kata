"""
ocr3 adaptor, used for testing

This module lets us test ocr3.py without having to know how ocr3.py works
internally.

"""

import os
import subprocess
import sys
import tempfile

python_exe = sys.executable
script = 'ocr3.py'

def run_ocr(input_string):
    """Given a string, give it to ocr3 as a file, and return the
    output of ocr3 as a string."""

    # create temporary file, write input string to file, and close file
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(input_string)
    temp_file.close()

    # call minesweeper with temporary file, while capturing standard out
    pipe = subprocess.Popen([python_exe, script, temp_file.name], 
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # get standard out
    output = pipe.communicate()[0]

    # delete temporary file
    os.unlink(temp_file.name)

    return output


