#########################################################
##  CS 4750 (Fall 2018), Assignment #1, Question #2    ##
##   Script File Name: tcomp2.py                       ##
##       Student Name: Nicholas Morgan                 ##
##         Login Name: njlm65                          ##
##              MUN #: 201335841                       ##
#########################################################

import sys

def nW(words):
    return len(words)

def sd(mainFile, compareFile):
    return mainFile ^ compareFile

def similarity(mainFile,compareFile):
    return 1.0 - float(nW(sd(mainFile,compareFile))) / (nW(mainFile) + nW(compareFile))

def main():
    if len(sys.argv) < 3:
        print "usage: python tcomp2.py filename file1name file2name ..."
        return
    master, files = sys.argv[1], sys.argv[2:]
    masterFile = set(open(master).read().replace('\n', ' ').split(' '))
    masterFile.remove('')
    similarities = []
    for file in files:
        compareFile = set(open(file).read().replace('\n', ' ').split(' '))
        compareFile.remove('')
        sim = similarity(masterFile, compareFile)
        similarities.append(sim)
        print ">>> Sim(\"{0}\", \"{1}\") = %.3f".format(master, file) % sim
    max_index = similarities.index(max(similarities))
    print "File \"{0}\" is most similar to file \"{1}\"".format(files[max_index], master)


if __name__== "__main__":
  main()
