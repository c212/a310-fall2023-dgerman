#!/usr/bin/python3

def trial(tries):
  count = 0
  for i in range(tries):
    # print(i, count)
    if i == 0:
      current = choice(["heads", "tails"])
      # print(i, current)
    else:
      current = choice(["heads", "tails"])
      # print(i, current)
      if past == current:
        count += 1
        if count == 6:
          # print(i)
          return 1
      else:
        count = 0
    past = current
  return 0

import sys

if (len(sys.argv) != 3):
  print("Usage: one number-of-coins number-of-trials")
  sys.exit(0)

tries = int(sys.argv[1])
trials = int(sys.argv[2])

from random import choice

sum = 0

for i in range(trials):
  sum += trial(tries)

print(sum/trials)
