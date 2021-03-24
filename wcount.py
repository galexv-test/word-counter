#!/usr/bin/env python3

import sys

def count_from_file(filename):
    nletters = 0
    nwords = 0
    npars = 0
    with open(filename, "rt") as fd:
        for par in fd:
            nletters += len(par)
            par = par.rstrip()
            npars += 1
            for word in par.split():
                nwords += 1
    return nletters, nwords, npars

if __name__=='__main__':
    if len(sys.argv)<2:
        print("Usage: wcount.py input_file.txt")
        sys.exit(1)
    nletters, nwords, npars = count_from_file(sys.argv[1])
    print(f"letters:{nletters} words:{nwords} paragraphs:{npars}")
    sys.exit(0)
