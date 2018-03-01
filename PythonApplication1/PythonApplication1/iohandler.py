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

def write_output(file_path, output):
    f = open(file_path, 'w')
    for i in range(len(output)):
        for j in range(len(output[i])):
            f.write(str(output[i][j]))
            f.write(' ')
        f.write('\n')

    f.close()