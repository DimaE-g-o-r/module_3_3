def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(8, 'cola', False)
print_params(466, 'водопад')
print_params(b = 25)
print_params(c = [1, 2, 3])


values_list = [1945, 'd', False]
values_dict = {'a': 250, 'b': 'trk', 'c': True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [230575, 'Дима']
print_params(*values_list_2, 42)
