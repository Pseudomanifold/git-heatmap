#!/usr/bin/env python3

import datetime
import subprocess
import sys

counts = [ [0]*24 for _ in range(7) ]

with open(sys.argv[1]) as f:
    for line in f:
        d   = datetime.datetime.fromtimestamp(int(line))
        row = d.weekday()
        col = d.hour

        counts[row][col] += 1

for row in range(7):
    for col in range(24):
        print("%d " % counts[row][col], end="")
    print("")
