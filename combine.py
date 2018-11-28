from sys import argv
import glob
import os

filenames = ['try4ma', 'trysrc', 'try4maout']


infilesbpe = glob.glob("/home/stefan/Downloads/Babel3.7/corpus/dev_tst/bpe_w/dev/*wBPE50")

print(infilesbpe)

infilesbpe = sorted(infilesbpe)

with open('dev.target.mfreBPE50', 'w') as outfile:
    for fname in infilesbpe:
        with open(fname) as infile:
            outfile.write(infile.read())
