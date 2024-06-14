#Так как после попытки print измененного кортежа выдаёт ошибку и не показывает
#print второй части. Я решил начать со списков.
mutable_list = [0, 1 ,'apple ', True, 7, 92]
print (mutable_list)
mutable_list[0] = 22
mutable_list [2] = 'two'
print (mutable_list)
immutable_var = 1, "Melon", True, 2, 4
print (immutable_var)
immutable_var [0] = "apple"  #Ошибка при print - TypeError: 'tuple' object does not support item assignment
print (immutable_var)       #Не получилось изменить т.к тип tup является неизменяемым типом данных