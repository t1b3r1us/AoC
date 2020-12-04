#!/usr/bin/env python3

import re
import os
path = "/Users/thomasmkirk/Documents/GitHub/AoC/2020/Day_04/"
os.chdir(path)

def get_data():
  with open("input.txt") as f:
    return [x for x in f.read().split("\n\n") if x]

def part1():
  part1 = 0
  fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
  for line in get_data():
    part1 += all(x in line for x in fields)
  return part1


def main():
  print(f'Part 1: {part1()}')
  return 0

if __name__ == '__main__':
  main()
