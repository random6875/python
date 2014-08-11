#!/usr/bin/python

import sys, getopt
import os
from os import listdir
from os.path import isfile, join
import datetime
import shutil

# main function
def main(argv):
    inputdir = ''
    outputdir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["idir=","odir="])
    except getopt.GetoptError:
        print 'test.py -i <inputdir> -o <outputdir>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputdir> -o <outputdir>'
            sys.exit()
        elif opt in ("-i", "--idir"):
            inputdir = arg
        elif opt in ("-o", "--odir"):
            outputdir = arg

    if outputdir=='':
        if inputdir=='':
            currentDir=os.getcwd()
            inputdir=outputdir=currentDir
            print 'Current directory is "', currentDir
        else:
            outputdir=inputdir

    print 'Input directory is "', inputdir
    print 'Output directory is "', outputdir
   
    onlyfiles = [ f for f in listdir(inputdir) if isfile(join(inputdir,f)) ]
    for file in onlyfiles:
        fullpath = join(inputdir,file)
        print fullpath
        t = os.path.getctime( fullpath)
        d = datetime.datetime.fromtimestamp(t)
        cdate="{0}-{1}-{2}".format(d.year,d.month,d.day)
        
        dirname=join(outputdir,cdate)
        try:
            os.makedirs(dirname)
        except OSError:
            if os.path.exists(dirname):
                # We are nearly safe
                pass
            else:
                # There was an error on creation, so make sure we know about it
                raise
        
        if os.path.exists(dirname):
            shutil.copy2(fullpath, dirname)
        print cdate
        
    print onlyfiles

if __name__ == "__main__":
   main(sys.argv[1:])
