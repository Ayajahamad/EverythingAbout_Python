# The os module provides dozens of functions for interacting with the operating system.

import os

"""
os.getcwd()     # Return the current working directory

os.chdir('/server/accesslogs')   # Change current working directory

os.system('mkdir today')   # Run the command mkdir in the system shell

dir(os)     # <returns a list of all module functions>

help(os)    # <returns an extensive manual page created from the module's docstrings>
"""

# The shutil module in Python provides a variety of high-level file operations, making it easier to perform tasks such as file copying, moving, and deleting.
import shutil

"""
# shutil.copyfile(src, dst)
shutil.copyfile('data.db', 'archive.db') # 'archive.db'

shutil.move('/build/executables', 'installdir') # 'installdir'
"""

# File Wildcards
# The glob module provides a function for making file lists from directory wildcard searches:

import glob

"""
glob.glob('*.py')
"""

#  Command Line Arguments
# Common utility scripts often need to process command line arguments. These arguments are stored in the sys module’s argv attribute as a list. For instance, let’s take the following demo.py file:

import sys

# print(sys.argv)

"""
The sys module also has attributes for stdin, stdout, and stderr. The latter is useful for emitting warnings and error messages to make them visible even when stdout has been redirected:

sys.stderr.write('Warning, log file not found starting a new one\n') # Warning, log file not found starting a new one
"""
# The most direct way to terminate a script is to use sys.exit().

# The math module gives access to the underlying C library functions for floating-point math:
import math

math.cos(math.pi / 4)   # 0.70710678118654757

math.log(1024, 2)   # 10.0

# The random module provides tools for making random selections:

import random

random.choice(['apple', 'pear', 'banana'])
# 'apple'
random.sample(range(100), 10)   # sampling without replacement
# [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
random.random()    # random float
# 0.17970987693706186
random.randrange(6)    # random integer chosen from range(6)
# 4

# The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

statistics.mean(data)   # 1.6071428571428572

statistics.median(data) # 1.25

statistics.variance(data)   # 1.3720238095238095v


# # There are a number of modules for accessing the internet and processing internet protocols. Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail:
from urllib.request import urlopen

with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline

# datetime: 2022-01-01T01:36:47.689215+00:00


# The datetime module supplies classes for manipulating dates and times in both simple and complex ways. While date and time arithmetic is supported, the focus of the implementation is on efficient member extraction for output formatting and manipulation. The module also supports objects that are timezone aware.


# dates are easily constructed and formatted
from datetime import date, datetime
now = date.today()

d = datetime.date(2003, 12, 2)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days
14368