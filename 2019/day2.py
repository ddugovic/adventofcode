from collections import defaultdict
import itertools
import math
from hashlib import md5
import msvcrt
import numpy as np
import os.path
import re
import sys

from intcode import Intcode


def get_input(filename=None):
  if not filename:
    filename = os.path.splitext(os.path.basename(__file__))[0] + '.txt'
  with open(filename) as fp:
    input = fp.read().rstrip()

  return list(map(int,input.split(',')))


def part1(input):
  prog = Intcode(input)
  prog[1] = 12
  prog[2] = 2
  prog.run()
  return prog[0]


def part2(input):
  for noun in range(100):
    for verb in range(100):
        prog = Intcode(input)
        prog[1] = noun
        prog[2] = verb
        prog.run()
        if prog[0] == 19690720:
          return 100 * noun + verb


if __name__ == '__main__':
  from argparse import ArgumentParser
  parser = ArgumentParser()
  parser.add_argument('input', nargs='?', metavar='input.txt')
  args = parser.parse_args()
  input = get_input(args.input)
  print(part1(input))
  print(part2(input))
