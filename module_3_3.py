#Задание 1
def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)

print_params()
print_params(555, 4)
print_params(b = 25)
print_params(c = [1, 2, 3])

#Задание 2
print('')
values_list = [110, 'rublei', 'dollae stoit epta']
values_dict = {'a': values_list[0], 'b': values_list[1], 'c': values_list[2]}
print_params(*values_list)
print_params(**values_dict)

#Задание 3
print('')
values_list_2 = [200, 'dollar skoro']
print_params(*values_list_2, 200)