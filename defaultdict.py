import collections

my_dict = collections.defaultdict(set)

fruits = [('apple', 'red'), ('banana', 'yellow'), ('apple', 'green')]

for fruit, color in fruits:
    my_dict[fruit].add(color)

print(my_dict)
