# -*- coding: utf-8 -*-
import sys
from operator import itemgetter
from itertools import groupby

def read_mapper_output(file):
    for line in file:
        yield line.split(',')

def main():
    data = read_mapper_output(sys.stdin)

    for key,group in groupby(data, itemgetter(0)):
        acc_price = 0
        acc_total = 0
        for athlete,sport,country,total,total_price in group:
            acc_price += int(total_price)
            acc_total += int(total)
        print athlete, (country, sport, acc_total, acc_price)

if __name__ == '__main__':
    main()
