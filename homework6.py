my_dict = {'Sasha': 2002, 'Anna': 2003, 'Egor': 2005}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Ivan'))
my_dict['Kirill'] = 2007
my_dict['Kristina'] = 2004
a = my_dict.pop('Egor')
print(a)
print(my_dict)
my_set = {1, 2, 3, 3, 6, 3, 0, 1, 4, 3, 2}
print(my_set)
my_set.add('Зелёный')                                         #B видео была возможность добавлять значения сразу в print
my_set.add(5)                               #на практике после того как я писал print(my_set.add(5)) в консоль выдавалось None
my_set.remove(3)
print(my_set)



