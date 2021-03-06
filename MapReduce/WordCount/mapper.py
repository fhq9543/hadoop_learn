#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
def read_input(file):
    for line in file:
        yield line.split()

def main():
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            print '%s\t%d' % (word, 1)

if __name__ == '__main__':
    main()
