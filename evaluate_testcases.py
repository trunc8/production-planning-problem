#!/usr/bin/env python

# trunc8 did this

import time
import glob # To get list of all testcase*.txt files
import os

# For multiprocessing
from subprocess import call
from functools import partial
from multiprocessing.dummy import Pool

# Fetching list of testcase files
DIR = "random_testcases"
files = glob.glob(DIR+"/testcase*.txt")

# Making list of all commands to be run
commands = []
for f in files:
  cmd = 'python3 linear_programming.py < ' + f
  commands.append(cmd)

start = time.time()
n = 40
pool = Pool(n) # n concurrent commands at a time
for i, returncode in enumerate(pool.imap(partial(call, shell=True), commands)):
  if returncode != 0:
    print("%d command failed: %d" % (i, returncode))

print(f"Time taken by LP method: {time.time() - start} seconds")


# Emptying commands list
commands = []
for f in files:
  if (os.path.isfile('a.out')):
    os.remove('a.out')
  os.system('g++ -O2 dynamic_programming.cpp')
  cmd = './a.out < ' + f
  commands.append(cmd)

start = time.time()
n = 40
pool = Pool(n) # n concurrent commands at a time
for i, returncode in enumerate(pool.imap(partial(call, shell=True), commands)):
  if returncode != 0:
    print("%d command failed: %d" % (i, returncode))

print(f"Time taken by DP method: {time.time() - start} seconds")