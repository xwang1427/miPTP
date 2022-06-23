#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import numpy as np
import pandas as pd


def write_to_svm(encodings, file):
    with open(file, 'w') as f:
        for line in encodings[1:]:
            line = line[1:]
            f.write('%s' % line[0])
            for i in range(1, len(line)):
                f.write('  %d:%s' % (i, line[i]))
            f.write('\n')


def write_to_tsv(encodings, file):
    with open(file, 'w') as f:
        for line in encodings[1:]:
            line = line[1:]
            f.write('%s' % line[0])
            for i in range(1, len(line)):
                f.write('\t%s' % line[i])
            f.write('\n')


def write_to_csv(encodings, file):
    with open(file, 'w') as f:
        for line in encodings[1:]:
            line = line[1:]
            f.write('%s' % line[0])
            for i in range(1, len(line)):
                f.write(',%s' % line[i])
            f.write('\n')


def save_file(encodings, format='svm', file='encodings.txt'):
    if encodings == 0:
        with open(file, 'w') as f:
            f.write('An error encountered.')
    else:
        if format == 'svm':
            write_to_svm(encodings, file)
        if format == 'tsv':
            write_to_tsv(encodings, file)
        if format == 'csv':
            write_to_csv(encodings, file)







