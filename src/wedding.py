"""
A set partitioning model of a wedding seating problem

"""

import pulp
import pandas as pd

max_tables = 15
max_table_size = 2
guests = '1 2 3 4 5 6 7 8 9 10 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31'.split()


# create list of all possible tables
possible_tables = [tuple(c) for c in pulp.allcombinations(guests,
                                                          max_table_size)]
del possible_tables[0:30]

happy=pd.read_csv('social_saving.csv',header=None)
happy=happy.values


def happiness(table):
    for i in range(len(possible_tables)):
        if possible_tables[i]==table:
            return happy[i][0]



# create a binary variable to state that a table setting is used
x = pulp.LpVariable.dicts('table', possible_tables,
                          lowBound=0,
                          upBound=1,
                          cat=pulp.LpInteger)

seating_model = pulp.LpProblem("Wedding Seating Model", pulp.LpMaximize)

seating_model += sum([happiness(table) * x[table] for table in possible_tables])

# specify the maximum number of tables
seating_model += sum([x[table] for table in possible_tables]) <= max_tables, \
                 "Maximum_number_of_tables"

# A guest must seated at one and only one table
for guest in guests:
    seating_model += sum([x[table] for table in possible_tables
                          if guest in table]) == 1, "Must_seat_%s" % guest

seating_model.solve()

print("The choosen tables are out of a total of %s:" % len(possible_tables))
for table in possible_tables:
    if x[table].value() == 1.0:
        print(table)