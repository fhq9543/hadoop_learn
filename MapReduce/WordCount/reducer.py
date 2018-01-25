#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter
from itertools import groupby
import sys

def read_mapper_output(file):
    for line in file:
        yield line.rstrip().split('\t', 1)

def main():
    data = read_mapper_output(sys.stdin)
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            print '%s\t%d' % (current_word, total_count)
        except ValueError:
            pass

if __name__ == '__main__':
    main()
