#########################################################
##  CS 4750 (Fall 2018), Assignment #1, Question #1    ##
##   Script File Name: tcomp1.py                       ##
##       Student Name: Nicholas Morgan                 ##
##         Login Name: njlm65                          ##
##              MUN #: 201335841                       ##
#########################################################

import sys

class File:
    def __init__(self, name, text, nGram = []):
        self.name = name
        self.text = text
        self.nGram = nGram

    def getNGram(self, n):
        for i in range(len(self.text) - n + 1):
            check = self.text[i:n + i]
            if ' ' not in check:
                self.nGram.append(check)

    def getFrequency(self, gram):
        return float(self.nGram.count(gram))/len(self.nGram)


def similarity(mainFile,compareFile):
    return float(1 - (difference(mainFile,compareFile)/2))


def difference(mainFile, compareFile):
    diff = 0
    totalGram = set(mainFile.nGram) | set(compareFile.nGram)
    for gram in totalGram:
        diff = diff + float(abs((mainFile.getFrequency(gram) if gram in mainFile.nGram else 0.0) - (compareFile.getFrequency(gram) if gram in compareFile.nGram else 0.0)))
    return diff


def main():
    if len(sys.argv) < 4:
        print "usage: python tcomp1.py filename n file1name file2name ..."
        return
    filesList = []
    n, files = sys.argv[2], sys.argv[3:]
    mainFile = File(sys.argv[1], open(sys.argv[1]).read().replace('\n', ' '), [])
    mainFile.getNGram(int(n))
    similarities = []
    for i in range(len(files)):
        filesList.append(File(files[i], open(files[i]).read().replace('\n', ' '), []))
        filesList[i].getNGram(int(n))
        sim = similarity(mainFile, filesList[i])
        similarities.append(sim)
        print ">>> Sim(\"{0}\", \"{1}\") = %.3f".format(mainFile.name, filesList[i].name) % sim
    max_index = similarities.index(max(similarities))
    print "File \"{0}\" is most similar to file \"{1}\"".format(files[max_index], mainFile.name)

if __name__== "__main__":
  main()
