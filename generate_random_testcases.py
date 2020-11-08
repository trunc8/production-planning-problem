#!/usr/bin/env python

# trunc8 did this

import random
import os
import numpy as np
import glob

NO_OF_TESTCASES = 10
DIR = "random_testcases"

random.seed(0)
# Assumption: all these values are int

# Empty random_testcases directory before adding new testcases
files = glob.glob(DIR+"/testcase*.txt")
for f in files:
  os.remove(f)

for i in range(NO_OF_TESTCASES):
  with open(os.path.join(DIR, f"testcase{i}.txt"), "w") as file:
    M = random.randint(1,12)
    D = np.zeros(M)
    for month in range(M):
      D[month] = random.randint(1,20)
    E = random.randint(1,10)
    Hcost = random.randint(20,50)
    Fcost = random.randint(20,50)
    S = random.randint(100,400)
    C = random.randint(1,10)
    OTC = random.randint(1,4)
    OTPrice = random.randint(30,200)
    W = random.randint(2,10)
    D_array = ' '.join(str(int(item)) for item in D)
    file.write(f"{M}\n{D_array}\n{E} {Hcost} {Fcost}\n{S} {C}\n{OTC} {OTPrice}\n{W}")
