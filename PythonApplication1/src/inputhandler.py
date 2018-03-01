import sys
import os

def read_input(file_path):
    print "dans read"
    print os.getcwd()
    f = open(file_path, 'r')
    entree = f.readlines()
    f.close()

    return [entree[i][]]
        entree[i] = entree[i][:-1]
    return entree

