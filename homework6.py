my_dict = {'Name1':2020, 'Name2':2021, 'Name3':2019}
print(my_dict)
print(my_dict.get('Name1'))
print(my_dict.get('Name76'))
my_dict.update({'Name4': 2022,
                'Name5':2021})
a = my_dict.pop('Name3')
print(a)
print(my_dict)

my_set = {1, 2, 3, 3, 6, 3, 0, 1, 4, 3, 2}
print(my_set)
my_set.add('Зелёный')
my_set.add('проверка')
my_set.remove(1)
print(my_set)



