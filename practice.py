my_dict = {'a': 5, 'b': 3, 'c': 8, 'd': 2}

#print key and values in reverse order
for key, value in (my_dict.items()):
    print(key, value)


#my_dict functions
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

#sort by key
for key in sorted(my_dict.keys()):
    print(key, my_dict[key])
    