import sys
import os

def read_input(file_path):
    print "dans read"
    print os.getcwd()
    f = open(file_path, 'r')
    entree = f.readlines()
    f.close()

    remove_line = [e[:-1] for e in entree]
    splited = [e.split() for e in remove_line]
    int_entree = [map(int, e) for e in splited]
    return int_entree
