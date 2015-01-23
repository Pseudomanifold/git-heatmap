#!/usr/bin/env python3

import argparse
import datetime
import subprocess
import os
import sys

parser = argparse.ArgumentParser(description="Create heatmaps of git commits")
parser.add_argument("--author",  help="Author whose git commits are to be counted", type=str)
parser.add_argument("directory", help="git directory to use", metavar="DIR")

arguments = parser.parse_args()

directory = os.path.join(arguments.directory, ".git")
author    = arguments.author or ""

commits   = subprocess.check_output( ["git", "--git-dir=%s" % directory,
                                             "log",
                                             "--pretty=format:%ct",
                                             "--author=%s" % author ] )
counts = [ [0]*24 for _ in range(7) ]

for commit in commits.decode().split():
    d   = datetime.datetime.fromtimestamp(int(commit))
    row = d.weekday()
    col = d.hour

    counts[row][col] += 1

for row in range(7):
    for col in range(24):
        print("%d " % counts[row][col], end="")
    print("")
