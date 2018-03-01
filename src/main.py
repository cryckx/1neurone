from inputhandler import *

entree = read_input("./example/a_example.in")

rows = entree[0][0]
columns = entree[0][1]
vehicles = entree[0][2]
rides = entree[0][3]
bonus = entree[0][4]
steps = entree[0][5]
ride_list = entree[1:]


print entree
print ride_list
print rows, columns, vehicles, rides, bonus, steps
